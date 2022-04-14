# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank_tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import bank_pb2 as bank__pb2
from . import coin_pb2 as coin__pb2
from .cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from .gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbank_tx.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\ncoin.proto\x1a\nbank.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xce\x01\n\x07MsgSend\x12.\n\x0c\x66rom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12,\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12[\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x11\n\x0fMsgSendResponse\"z\n\x0cMsgMultiSend\x12\x30\n\x06inputs\x18\x01 \x03(\x0b\x32\x1a.cosmos.bank.v1beta1.InputB\x04\xc8\xde\x1f\x00\x12\x32\n\x07outputs\x18\x02 \x03(\x0b\x32\x1b.cosmos.bank.v1beta1.OutputB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00\"\x16\n\x14MsgMultiSendResponse2\xac\x01\n\x03Msg\x12J\n\x04Send\x12\x1c.cosmos.bank.v1beta1.MsgSend\x1a$.cosmos.bank.v1beta1.MsgSendResponse\x12Y\n\tMultiSend\x12!.cosmos.bank.v1beta1.MsgMultiSend\x1a).cosmos.bank.v1beta1.MsgMultiSendResponseB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')



_MSGSEND = DESCRIPTOR.message_types_by_name['MsgSend']
_MSGSENDRESPONSE = DESCRIPTOR.message_types_by_name['MsgSendResponse']
_MSGMULTISEND = DESCRIPTOR.message_types_by_name['MsgMultiSend']
_MSGMULTISENDRESPONSE = DESCRIPTOR.message_types_by_name['MsgMultiSendResponse']
MsgSend = _reflection.GeneratedProtocolMessageType('MsgSend', (_message.Message,), {
  'DESCRIPTOR' : _MSGSEND,
  '__module__' : 'bank_tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgSend)
  })
_sym_db.RegisterMessage(MsgSend)

MsgSendResponse = _reflection.GeneratedProtocolMessageType('MsgSendResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDRESPONSE,
  '__module__' : 'bank_tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgSendResponse)
  })
_sym_db.RegisterMessage(MsgSendResponse)

MsgMultiSend = _reflection.GeneratedProtocolMessageType('MsgMultiSend', (_message.Message,), {
  'DESCRIPTOR' : _MSGMULTISEND,
  '__module__' : 'bank_tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgMultiSend)
  })
_sym_db.RegisterMessage(MsgMultiSend)

MsgMultiSendResponse = _reflection.GeneratedProtocolMessageType('MsgMultiSendResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGMULTISENDRESPONSE,
  '__module__' : 'bank_tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgMultiSendResponse)
  })
_sym_db.RegisterMessage(MsgMultiSendResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
  _MSGSEND.fields_by_name['from_address']._options = None
  _MSGSEND.fields_by_name['from_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSEND.fields_by_name['to_address']._options = None
  _MSGSEND.fields_by_name['to_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSEND.fields_by_name['amount']._options = None
  _MSGSEND.fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGSEND._options = None
  _MSGSEND._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGMULTISEND.fields_by_name['inputs']._options = None
  _MSGMULTISEND.fields_by_name['inputs']._serialized_options = b'\310\336\037\000'
  _MSGMULTISEND.fields_by_name['outputs']._options = None
  _MSGMULTISEND.fields_by_name['outputs']._serialized_options = b'\310\336\037\000'
  _MSGMULTISEND._options = None
  _MSGMULTISEND._serialized_options = b'\350\240\037\000'
  _MSGSEND._serialized_start=112
  _MSGSEND._serialized_end=318
  _MSGSENDRESPONSE._serialized_start=320
  _MSGSENDRESPONSE._serialized_end=337
  _MSGMULTISEND._serialized_start=339
  _MSGMULTISEND._serialized_end=461
  _MSGMULTISENDRESPONSE._serialized_start=463
  _MSGMULTISENDRESPONSE._serialized_end=485
  _MSG._serialized_start=488
  _MSG._serialized_end=660
# @@protoc_insertion_point(module_scope)