# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keys.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmospy.generated.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nkeys.proto\x12\x17\x63osmos.crypto.secp256k1\x1a\x14gogoproto/gogo.proto\"\x1b\n\x06PubKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c:\x04\x98\xa0\x1f\x00\"\x16\n\x07PrivKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x42\x34Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1b\x06proto3')



_PUBKEY = DESCRIPTOR.message_types_by_name['PubKey']
_PRIVKEY = DESCRIPTOR.message_types_by_name['PrivKey']
PubKey = _reflection.GeneratedProtocolMessageType('PubKey', (_message.Message,), {
  'DESCRIPTOR' : _PUBKEY,
  '__module__' : 'keys_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.secp256k1.PubKey)
  })
_sym_db.RegisterMessage(PubKey)

PrivKey = _reflection.GeneratedProtocolMessageType('PrivKey', (_message.Message,), {
  'DESCRIPTOR' : _PRIVKEY,
  '__module__' : 'keys_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.secp256k1.PrivKey)
  })
_sym_db.RegisterMessage(PrivKey)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1'
  _PUBKEY._options = None
  _PUBKEY._serialized_options = b'\230\240\037\000'
  _PUBKEY._serialized_start=61
  _PUBKEY._serialized_end=88
  _PRIVKEY._serialized_start=90
  _PRIVKEY._serialized_end=112
# @@protoc_insertion_point(module_scope)
