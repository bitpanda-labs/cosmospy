import base64
from binascii import Error as B64DecodingError
import hashlib
from typing import List, Optional, TypedDict, Union

from google.protobuf.message import DecodeError

from .generated.bank_pb2 import Input, Output
from .generated.bank_tx_pb2 import MsgMultiSend, MsgSend
from .generated.coin_pb2 import Coin
from .generated.tx_pb2 import Fee, Tx, TxBody


class DecodedAmount(TypedDict):
    amount: str
    denom: str


class DecodedInputOutput(TypedDict):
    address: str
    coins: List[DecodedAmount]


class DecodedMultiSend(TypedDict):
    inputs: List[DecodedInputOutput]
    outputs: List[DecodedInputOutput]


class DecodedSend(TypedDict):
    from_address: str
    to_address: str
    amount: List[DecodedAmount]


class DecodedMessage(TypedDict):
    type: str
    content: Optional[Union[DecodedSend, DecodedMultiSend]]


class DecodedBody(TypedDict):
    messages: List[DecodedMessage]
    memo: str


class DecodedFee(TypedDict):
    amount: List[DecodedAmount]
    gas_limit: int


class DecodedTransaction(TypedDict):
    id: str
    body: DecodedBody
    fee: DecodedFee
    signatures: List[bytes]


def _decode_amount(coin: Coin) -> DecodedAmount:
    return DecodedAmount(amount=coin.amount, denom=coin.denom)


def _decode_inputs_outputs(inputs_outputs: List[Union[Input, Output]]) -> List[DecodedInputOutput]:
    return [
        DecodedInputOutput(
            address=item.address,
            coins=[_decode_amount(coin) for coin in item.coins]
        ) for item in inputs_outputs
    ]


def _decode_multi_send(send_bytes: bytes) -> DecodedMultiSend:
    send = MsgMultiSend()
    send.ParseFromString(send_bytes)
    return DecodedMultiSend(
        inputs=_decode_inputs_outputs(send.inputs),
        outputs=_decode_inputs_outputs(send.outputs),
    )


def _decode_send(send_bytes: bytes) -> DecodedSend:
    send = MsgSend()
    send.ParseFromString(send_bytes)
    return DecodedSend(
        amount=[_decode_amount(amount) for amount in send.amount],
        to_address=send.to_address,
        from_address=send.from_address,
    )


def _decode_body(body: TxBody) -> DecodedBody:
    result = DecodedBody(messages=[], memo=body.memo)
    for message in body.messages:
        msg = DecodedMessage(
            type=message.type_url,
            content=None,
        )
        if message.type_url == "/cosmos.bank.v1beta1.MsgSend":
            msg["content"] = _decode_send(message.value)
        if message.type_url == "/cosmos.bank.v1beta1.MsgMultiSend":
            msg["content"] = _decode_multi_send(message.value)
        result["messages"].append(msg)
    return result


def _decode_fee(fee: Fee) -> DecodedFee:
    return DecodedFee(
        amount=[_decode_amount(amount) for amount in fee.amount],
        gas_limit=fee.gas_limit,
    )


def get_tx_hash(b64_tx: str) -> str:
    tx_bytes = base64.b64decode(b64_tx)
    return hashlib.sha256(tx_bytes).hexdigest()


def decode_transaction(b64_tx: str) -> DecodedTransaction:
    try:
        tx_bytes = base64.b64decode(b64_tx)
    except B64DecodingError as e:
        raise ValueError(f"Failed to decode b64 string. Please provide a valid base64 encoded string. Error: {e}")
    try:
        transaction = Tx()
        transaction.ParseFromString(tx_bytes)
    except DecodeError as e:
        raise ValueError(f"Failed to decode transaction. Please provide a valid cosmos transaction. Error: {e}")

    return DecodedTransaction(
        id=get_tx_hash(b64_tx),
        fee=_decode_fee(transaction.auth_info.fee),
        body=_decode_body(transaction.body),
        signatures=transaction.signatures,
    )
