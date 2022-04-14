from base64 import b64encode
from unittest.mock import Mock

from ward import test

from src.cosmospy import Transaction


@test("sign transaction")
def _():
    private_key = bytes.fromhex("2afc5a66b30e7521d553ec8e6f7244f906df97477248c30c103d7b3f2c671fef")
    unordered_sign_message = {
        "chain_id": "tendermint_test",
        "account_number": "1",
        "fee": {"gas": "21906", "amount": [{"amount": "0", "denom": ""}]},
        "memo": "",
        "sequence": "0",
        "msgs": [
            {
                "type": "cosmos-sdk/Send",
                "value": {
                    "inputs": [
                        {
                            "address": "cosmos1qperwt9wrnkg5k9e5gzfgjppzpqhyav5j24d66",
                            "coins": [{"amount": "1", "denom": "STAKE"}],
                        }
                    ],
                    "outputs": [
                        {
                            "address": "cosmos1yeckxz7tapz34kjwnjxvmxzurerquhtrmxmuxt",
                            "coins": [{"amount": "1", "denom": "STAKE"}],
                        }
                    ],
                },
            }
        ],
    }
    dummy_num = 1337
    tx = Transaction(
        privkey=private_key,
        account_num=dummy_num,
        sequence=dummy_num,
        fee=dummy_num,
        gas=dummy_num,
    )
    tx._get_sign_message = Mock(return_value=unordered_sign_message)

    expected_signature = (
        "vqjcPpVDEA17fUiLQbTqPaXoIxilhfigDx4KNG546n5vQUz9mc4/Sztk0t3saw+iYkoE3MRLSbO9S0BcQQ0D7A=="
    )

    actual_signature = b64encode(tx._get_signatures()).decode()
    assert actual_signature == expected_signature


@test("make transaction pushable to the RPC API")  # type: ignore[no-redef]
def _():
    expected_pushable_tx = '{"jsonrpc": "2.0", "id": 1, "method": "broadcast_tx_sync", "params": {"tx": "CpIBCo8BChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEm8KLWNvc21vczFsZ2hhcnpnZHM4OWxwc2hyN3E4a2NtZDJlc254a2Zwd3Z1ejV0chItY29zbW9zMTAzbDc1OHBzNzQwM3NkOWMweThqNmhyZnc0eHlsNzBqNG1td2tmGg8KBXVhdG9tEgYzODcwMDASZQpOCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohA49sjCd3Eul+ZXyof7qO460UaO73otrmySHyTNSLW+XnEgQKAggBEhMKDQoFdWF0b20SBDEwMDAQiKECGkDfbtF0GoJzi9S1YVOjgGZohl+64x5A2L56iHZQJm7HUgwSCDxdeNZmif2RaBMd7APdv+h6wWoTES9RjEHKYgg4"}}'  # noqa: E501
    tx = create_tx()
    pushable_tx = tx.get_pushable_rpc()
    assert pushable_tx == expected_pushable_tx


@test("make transaction pushable to the HTTP API")  # type: ignore[no-redef]
def _():
    expected_pushable_tx = '{"tx_bytes": "CpIBCo8BChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEm8KLWNvc21vczFsZ2hhcnpnZHM4OWxwc2hyN3E4a2NtZDJlc254a2Zwd3Z1ejV0chItY29zbW9zMTAzbDc1OHBzNzQwM3NkOWMweThqNmhyZnc0eHlsNzBqNG1td2tmGg8KBXVhdG9tEgYzODcwMDASZQpOCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohA49sjCd3Eul+ZXyof7qO460UaO73otrmySHyTNSLW+XnEgQKAggBEhMKDQoFdWF0b20SBDEwMDAQiKECGkDfbtF0GoJzi9S1YVOjgGZohl+64x5A2L56iHZQJm7HUgwSCDxdeNZmif2RaBMd7APdv+h6wWoTES9RjEHKYgg4", "mode": "broadcast_tx_sync"}'  # noqa: E501
    tx = create_tx()
    pushable_tx = tx.get_pushable_api()
    assert pushable_tx == expected_pushable_tx


def create_tx():
    _tx_total_cost = 388000
    fee = 1000
    amount = _tx_total_cost - fee

    tx = Transaction(
        privkey=bytes.fromhex("26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59"),
        account_num=11335,
        sequence=0,
        fee=fee,
        gas=37000,
        chain_id="cosmoshub-2",
    )
    tx.add_transfer(recipient="cosmos103l758ps7403sd9c0y8j6hrfw4xyl70j4mmwkf", amount=amount)
    return tx
