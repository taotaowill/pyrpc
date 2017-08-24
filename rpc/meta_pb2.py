# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='meta.proto',
  package='pyrpc.rpc',
  serialized_pb=_b('\n\nmeta.proto\x12\tpyrpc.rpc\"V\n\x07RpcMeta\x12\x13\n\x0bsequence_id\x18\x01 \x02(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x12\n\nerror_code\x18\x04 \x01(\x05\x12\x12\n\nerror_text\x18\x05 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RPCMETA = _descriptor.Descriptor(
  name='RpcMeta',
  full_name='pyrpc.rpc.RpcMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_id', full_name='pyrpc.rpc.RpcMeta.sequence_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='pyrpc.rpc.RpcMeta.method', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='pyrpc.rpc.RpcMeta.error_code', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_text', full_name='pyrpc.rpc.RpcMeta.error_text', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['RpcMeta'] = _RPCMETA

RpcMeta = _reflection.GeneratedProtocolMessageType('RpcMeta', (_message.Message,), dict(
  DESCRIPTOR = _RPCMETA,
  __module__ = 'meta_pb2'
  # @@protoc_insertion_point(class_scope:pyrpc.rpc.RpcMeta)
  ))
_sym_db.RegisterMessage(RpcMeta)


# @@protoc_insertion_point(module_scope)
