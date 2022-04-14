from . import Transaction

tx = Transaction(
    privkey=bytes.fromhex(
        "26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59"
    ),
    account_num=11335,
    sequence=0,
    fee=1000,
    gas=70000,
    memo="",
    chain_id="cosmoshub-4",
)
tx.add_transfer(
    recipient="cosmos103l758ps7403sd9c0y8j6hrfw4xyl70j4mmwkf", amount=387000
)
pushable = tx.get_pushable_rpc()
import requests

pushable_tx = tx.get_pushable_rpc()
print(pushable_tx)
r = requests.post("https://rpc.cosmos.smartnodes.one", data=pushable_tx)
print(r.text)