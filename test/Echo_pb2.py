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
  package='pyrpc.test',
  serialized_pb=_b('\n\nEcho.proto\x12\npyrpc.test\"\x1e\n\x0b\x45\x63hoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0c\x45\x63hoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1a\n\nSumRequest\x12\x0c\n\x04nums\x18\x01 \x03(\x03\"\x1a\n\x0bSumResponse\x12\x0b\n\x03sum\x18\x01 \x02(\x03\x32H\n\x0b\x45\x63hoService\x12\x39\n\x04\x45\x63ho\x12\x17.pyrpc.test.EchoRequest\x1a\x18.pyrpc.test.EchoResponse2F\n\nSumService\x12\x38\n\x05\x43ount\x12\x16.pyrpc.test.SumRequest\x1a\x17.pyrpc.test.SumResponseB\x03\x90\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='pyrpc.test.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pyrpc.test.EchoRequest.message', index=0,
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
  serialized_start=26,
  serialized_end=56,
)


_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='pyrpc.test.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pyrpc.test.EchoResponse.message', index=0,
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
  serialized_start=58,
  serialized_end=89,
)


_SUMREQUEST = _descriptor.Descriptor(
  name='SumRequest',
  full_name='pyrpc.test.SumRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nums', full_name='pyrpc.test.SumRequest.nums', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=91,
  serialized_end=117,
)


_SUMRESPONSE = _descriptor.Descriptor(
  name='SumResponse',
  full_name='pyrpc.test.SumResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sum', full_name='pyrpc.test.SumResponse.sum', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=119,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE
DESCRIPTOR.message_types_by_name['SumRequest'] = _SUMREQUEST
DESCRIPTOR.message_types_by_name['SumResponse'] = _SUMRESPONSE

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:pyrpc.test.EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:pyrpc.test.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)

SumRequest = _reflection.GeneratedProtocolMessageType('SumRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUMREQUEST,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:pyrpc.test.SumRequest)
  ))
_sym_db.RegisterMessage(SumRequest)

SumResponse = _reflection.GeneratedProtocolMessageType('SumResponse', (_message.Message,), dict(
  DESCRIPTOR = _SUMRESPONSE,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:pyrpc.test.SumResponse)
  ))
_sym_db.RegisterMessage(SumResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='pyrpc.test.EchoService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=147,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='pyrpc.test.EchoService.Echo',
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



_SUMSERVICE = _descriptor.ServiceDescriptor(
  name='SumService',
  full_name='pyrpc.test.SumService',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=221,
  serialized_end=291,
  methods=[
  _descriptor.MethodDescriptor(
    name='Count',
    full_name='pyrpc.test.SumService.Count',
    index=0,
    containing_service=None,
    input_type=_SUMREQUEST,
    output_type=_SUMRESPONSE,
    options=None,
  ),
])

SumService = service_reflection.GeneratedServiceType('SumService', (_service.Service,), dict(
  DESCRIPTOR = _SUMSERVICE,
  __module__ = 'Echo_pb2'
  ))

SumService_Stub = service_reflection.GeneratedServiceStubType('SumService_Stub', (SumService,), dict(
  DESCRIPTOR = _SUMSERVICE,
  __module__ = 'Echo_pb2'
  ))


# @@protoc_insertion_point(module_scope)
