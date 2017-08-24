# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Echo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Echo.proto',
  package='pyrpc.proto',
  serialized_pb=_b('\n\nEcho.proto\x12\x0bpyrpc.proto\"\x1e\n\x0b\x45\x63hoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0c\x45\x63hoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2J\n\x0b\x45\x63hoService\x12;\n\x04\x45\x63ho\x12\x18.pyrpc.proto.EchoRequest\x1a\x19.pyrpc.proto.EchoResponseB\x03\x90\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='pyrpc.proto.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pyrpc.proto.EchoRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=27,
  serialized_end=57,
)


_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='pyrpc.proto.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pyrpc.proto.EchoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=59,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:pyrpc.proto.EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:pyrpc.proto.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='pyrpc.proto.EchoService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=92,
  serialized_end=166,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='pyrpc.proto.EchoService.Echo',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHORESPONSE,
    options=None,
  ),
])

EchoService = service_reflection.GeneratedServiceType('EchoService', (_service.Service,), dict(
  DESCRIPTOR = _ECHOSERVICE,
  __module__ = 'Echo_pb2'
  ))

EchoService_Stub = service_reflection.GeneratedServiceStubType('EchoService_Stub', (EchoService,), dict(
  DESCRIPTOR = _ECHOSERVICE,
  __module__ = 'Echo_pb2'
  ))


# @@protoc_insertion_point(module_scope)
