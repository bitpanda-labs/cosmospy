from __future__ import annotations

import base64
import hashlib
import json
from typing import Any

import ecdsa

from cosmospy._wallet import DEFAULT_BECH32_HRP, privkey_to_address, privkey_to_pubkey
from cosmospy.typing import SyncModeApi, SyncModeRpc

from cosmospy.generated import  bank_tx_pb2 as bank_msg
from cosmospy.generated import coin_pb2 as coin
from cosmospy.generated import tx_pb2 as tx
from cosmospy.generated import keys_pb2 as keys
from cosmospy.generated import any_pb2 as any



class Transaction:
    """A Cosmos transaction.

    After initialization, one or more token transfers can be added by
    calling the `add_transfer()` method. Finally, call `get_pushable()`
    to get a signed transaction that can be pushed to the `POST /txs`
    endpoint of the Cosmos REST API.
    """

    def __init__(
        self,
        *,
        privkey: bytes,
        account_num: int,
        sequence: int,
        fee: int,
        gas: int,
        fee_denom: str = "uatom",
        memo: str = "",
        chain_id: str = "cosmoshub-4",
        hrp: str = DEFAULT_BECH32_HRP,
        sync_mode_api: SyncModeApi = "sync",
        sync_mode_rpc: SyncModeRpc = "broadcast_tx_sync",
    ) -> None:
        self._tx_body = tx.TxBody()
        self._tx_raw = tx.TxRaw()
        self._privkey = privkey
        self._account_num = account_num
        self._sequence = sequence
        self._fee = fee
        self._fee_denom = fee_denom
        self._gas = gas
        self._memo = memo
        self._chain_id = chain_id
        self._hrp = hrp
        self._sync_mode_rpc = sync_mode_rpc
        self._sync_mode_api = sync_mode_api


    def add_transfer(self, recipient: str, amount: int, denom: str = "uatom") -> None:
        msg = bank_msg.MsgSend()
        msg.from_address = privkey_to_address(self._privkey, hrp=self._hrp)
        msg.to_address = recipient

        amount = coin.Coin()
        amount.denom = "6"
        amount.amount = str(amount)

        msg.amount.append(amount)

        msg_any = any.Any()
        msg_any.Pack(msg)
        msg_any.type_url = "/cosmos.bank.v1beta1.MsgSend"
        self._tx_body.messages.append(msg_any)

    def get_pushable_rpc(self) -> str:
        self._tx_raw.body_bytes = self._tx_body.SerializeToString()
        self._tx_raw.auth_info_bytes = self._get_auth_info().SerializeToString()
        self._tx_raw.signatures.append(self._get_signatures())
        raw_tx = self._tx_raw.SerializeToString()
        tx_bytes = bytes(raw_tx)
        tx_b64 = base64.b64encode(tx_bytes).decode("utf-8")
        return json.dumps(
            {"jsonrpc": "2.0", "id": 1, "method": self._sync_mode_rpc, "params": {"tx": tx_b64}}
        )

    def get_pushable_api(self) -> str:
        self._tx_raw.body_bytes = self._tx_body.SerializeToString()
        self._tx_raw.auth_info_bytes = self._get_auth_info().SerializeToString()
        self._tx_raw.signatures.append(self._get_signatures())
        raw_tx = self._tx_raw.SerializeToString()
        tx_bytes = bytes(raw_tx)
        tx_b64 = base64.b64encode(tx_bytes).decode("utf-8")
        return json.dumps(
            {
                "tx_bytes": tx_b64,
                "mode": self._sync_mode_rpc
            }
        )


    def _get_signatures(self):
        privkey = ecdsa.SigningKey.from_string(self._privkey, curve=ecdsa.SECP256k1)
        signature_compact = privkey.sign_deterministic(
            self._get_sign_doc().SerializeToString(),
            hashfunc=hashlib.sha256,
            sigencode=ecdsa.util.sigencode_string_canonize,
        )
        return signature_compact

    def _get_sign_doc(self):
        sign_doc = tx.SignDoc()
        sign_doc.body_bytes = self._tx_body.SerializeToString()
        sign_doc.auth_info_bytes = self._get_auth_info().SerializeToString()
        sign_doc.chain_id = self._chain_id
        sign_doc.account_number = self._account_num
        return sign_doc

    def _get_auth_info(self):
        auth_info = tx.AuthInfo()
        auth_info.signer_infos.append(self._get_signer_infos(self._get_pubkey()))
        auth_info.fee.gas_limit = self._gas
        auth_info.fee.amount.append(self._get_fee())
        return auth_info

    def _get_fee(self):
        fee = coin.Coin()
        fee.amount = str(self._fee)
        fee.denom = self._fee_denom
        return fee

    def _get_pubkey(self):
        pubkey_bytes = privkey_to_pubkey(self._privkey)
        pubkey = keys.PubKey()
        pubkey.key = pubkey_bytes
        return pubkey

    def _get_signer_infos(self, _pubkey):
        signer_infos = tx.SignerInfo()
        signer_infos.sequence = self._sequence
        signer_infos.public_key.Pack(_pubkey)
        signer_infos.public_key.type_url = "/cosmos.crypto.secp256k1.PubKey"
        signer_infos.mode_info.single.mode = 1
        return signer_infos

