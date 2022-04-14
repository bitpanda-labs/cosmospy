from ward import test

from src.cosmospy import decode_transaction


@test("decode send transaction")
def _():
    send_transaction = "CpMBCpABChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEnAKLWNvc21vczF0NXUwamZnM2xqc2pyaDJtOWU0N2Q0bnkyaGVhN2VlaHhyemRnZBItY29zbW9zMWtlZzVmbnVjcDY5NG54MzRwM3NxMjc2bHY4NWQ1dGR0OHVxbWZ1GhAKBXVhdG9tEgc5NzI1ODI1EmkKUgpGCh8vY29zbW9zLmNyeXB0by5zZWNwMjU2azEuUHViS2V5EiMKIQLqGodLEwWelzPDXpDLKlhlpGtk7ZDSVVR8B8pSOSf8YhIECgIIfxjwpSQSEwoNCgV1YXRvbRIEMjUwMBCImAUaQDwPUK7ozUOPlSVLXO1QujlzaZXKSUVtNyJnFpatyUs1Z5ojQ2mOQu9liEIKthoVm4bCRY+hzJB6o0rOWA92NPU="  # noqa: E501
    decoded = decode_transaction(send_transaction)
    messages = decoded.get("body", {}).get("messages", [])
    assert decoded.get("id") == "a73082e0879aa34706a6a773578f8be740b31945e743bfe747eda7dcdef3703f"
    assert len(messages) == 1
    assert messages[0].get("type") == "/cosmos.bank.v1beta1.MsgSend"
    assert messages[0].get("content", {}).get("to_address") == "cosmos1keg5fnucp694nx34p3sq276lv85d5tdt8uqmfu"


@test("decode multi-send transaction")
def _():
    multi_send_transaction = "CrMBCrABCiEvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dNdWx0aVNlbmQSigEKQwotY29zbW9zMWQzM2VqNXgwZnQ0bXR6a3U0bDM4dWY1em0wY3ljNGVubXczNzJ2EhIKBXVhdG9tEgkxMTA1NTYwMDASQwotY29zbW9zMTQ0ZnpwZXB1dmRmdHY0dTRyOWtxOHQzNWFwMmNycnV2NHUzdWR6EhIKBXVhdG9tEgkxMTA1NTYwMDASZQpOCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohAwPBr6kwbQyJRxoy3RYE/84dwFLJoRSOI4PsynwBi4aMEgQKAgh/EhMKDQoFdWF0b20SBDEwMDAQwJoMGkDnMHAS0q2r6wSLQfM4MpWU5HxMpsSUbbYr6B5g2W35MzW4YPPKJBwEZmc1exlXkxv0VPKM6YpK9ASiPAyBtMOr"  # noqa: E501
    decoded = decode_transaction(multi_send_transaction)
    messages = decoded.get("body", {}).get("messages", [])
    content = messages[0].get("content", {})
    assert decoded.get("id") == "642daea1e32cb79439d7dd0a392a9aaa39454ff593a95ebf0b3220261adfd0de"
    assert len(messages) == 1
    assert messages[0].get("type") == "/cosmos.bank.v1beta1.MsgMultiSend"
    assert content.get("inputs")[0].get("address") == "cosmos1d33ej5x0ft4mtzku4l38uf5zm0cyc4enmw372v"
    assert content.get("outputs")[0].get("address") == "cosmos144fzpepuvdftv4u4r9kq8t35ap2crruv4u3udz"


@test("decode multi-message transaction")
def _():
    multi_msg_transaction = "CsMCCqABCjcvY29zbW9zLmRpc3RyaWJ1dGlvbi52MWJldGExLk1zZ1dpdGhkcmF3RGVsZWdhdG9yUmV3YXJkEmUKLWNvc21vczF0Z2tnZmVxNjhxdTQzY2x4MnBtMGh0bDlsdHNrcTg3cXF3M2ZsdRI0Y29zbW9zdmFsb3BlcjFnNDgyNjhtdTV2ZnA0d2s3ZGs4OXIwd2RyYWttOXA1eGswcTUwawqdAQojL2Nvc21vcy5zdGFraW5nLnYxYmV0YTEuTXNnRGVsZWdhdGUSdgotY29zbW9zMXRna2dmZXE2OHF1NDNjbHgycG0waHRsOWx0c2txODdxcXczZmx1EjRjb3Ntb3N2YWxvcGVyMWc0ODI2OG11NXZmcDR3azdkazg5cjB3ZHJha205cDV4azBxNTBrGg8KBXVhdG9tEgYxMTEzMTgSZgpQCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohA9zzwIwAiU/s7lrTgnatxXcKrfq8MuAa+tGY6xWdvSgZEgQKAggBGBASEgoMCgV1YXRvbRIDNzUwEOCnEhpAqJHVNdQn/G2KRme/w/onKNZi1GhFehyVzG5RpDJM7wVBQl17PalxdV6+BFSHh00K4BBm9k6vRPTvyDK7Z2oynw=="  # noqa: E501
    decoded = decode_transaction(multi_msg_transaction)
    messages = decoded.get("body", {}).get("messages", [])
    assert decoded.get("id") == "c0f9032d516a55b977444f08fe7ab8260ddbe495d4c7467feb544eb411712685"
    assert len(messages) > 1
    assert messages[0].get("content") is None


@test("decode invalid base64")
def _():
    invalid_b64 = "CsMCCqABCjcvY29zbW9zLmRpc3RyaWJ1dlv"
    try:
        decode_transaction(invalid_b64)
    except ValueError as e:
        assert "Failed to decode b64" in str(e)
        return
    raise Exception("Decoder should raise for invalid base64 string")


@test("decode invalid transaction")
def _():
    invalid_transaction = "CsMCCqABCjcvY29zbW9zLmRpc3RyaWJ1dGlv"
    try:
        decode_transaction(invalid_transaction)
    except ValueError as e:
        assert "Failed to decode transaction" in str(e)
        return
    raise Exception("Decoder should raise for invalid transaction")
