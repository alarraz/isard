# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/grpc/proto/bases_stream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/grpc/proto/bases_stream.proto',
  package='bases_stream',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!api/grpc/proto/bases_stream.proto\x12\x0c\x62\x61ses_stream\"\x0f\n\rStreamRequest\"\xe6\x01\n\x0eStreamResponse\x12\x0f\n\x07\x62\x61se_id\x18\x01 \x01(\t\x12\x31\n\x05state\x18\x02 \x01(\x0e\x32\".bases_stream.StreamResponse.State\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12\x14\n\x0cnext_actions\x18\x04 \x03(\t\x12\x0c\n\x04kind\x18\x05 \x01(\t\"\\\n\x05State\x12\x0b\n\x07STOPPED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0b\n\x07\x44\x45LETED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07UNKNOWN\x10\x05\x12\x07\n\x03NEW\x10\x06\x32W\n\x0b\x42\x61sesStream\x12H\n\x07\x43hanges\x12\x1b.bases_stream.StreamRequest\x1a\x1c.bases_stream.StreamResponse\"\x00\x30\x01\x62\x06proto3')
)



_STREAMRESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='bases_stream.StreamResponse.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=207,
  serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_STREAMRESPONSE_STATE)


_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='bases_stream.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=66,
)


_STREAMRESPONSE = _descriptor.Descriptor(
  name='StreamResponse',
  full_name='bases_stream.StreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_id', full_name='bases_stream.StreamResponse.base_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='bases_stream.StreamResponse.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='bases_stream.StreamResponse.detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_actions', full_name='bases_stream.StreamResponse.next_actions', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='bases_stream.StreamResponse.kind', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STREAMRESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=299,
)

_STREAMRESPONSE.fields_by_name['state'].enum_type = _STREAMRESPONSE_STATE
_STREAMRESPONSE_STATE.containing_type = _STREAMRESPONSE
DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['StreamResponse'] = _STREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMREQUEST,
  '__module__' : 'api.grpc.proto.bases_stream_pb2'
  # @@protoc_insertion_point(class_scope:bases_stream.StreamRequest)
  })
_sym_db.RegisterMessage(StreamRequest)

StreamResponse = _reflection.GeneratedProtocolMessageType('StreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMRESPONSE,
  '__module__' : 'api.grpc.proto.bases_stream_pb2'
  # @@protoc_insertion_point(class_scope:bases_stream.StreamResponse)
  })
_sym_db.RegisterMessage(StreamResponse)



_BASESSTREAM = _descriptor.ServiceDescriptor(
  name='BasesStream',
  full_name='bases_stream.BasesStream',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=301,
  serialized_end=388,
  methods=[
  _descriptor.MethodDescriptor(
    name='Changes',
    full_name='bases_stream.BasesStream.Changes',
    index=0,
    containing_service=None,
    input_type=_STREAMREQUEST,
    output_type=_STREAMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BASESSTREAM)

DESCRIPTOR.services_by_name['BasesStream'] = _BASESSTREAM

# @@protoc_insertion_point(module_scope)
