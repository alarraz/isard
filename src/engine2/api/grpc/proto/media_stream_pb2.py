# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/grpc/proto/media_stream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/grpc/proto/media_stream.proto',
  package='templates_stream',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!api/grpc/proto/media_stream.proto\x12\x10templates_stream\"\x14\n\x12MediaStreamRequest\"\xe7\x01\n\x13MediaStreamResponse\x12\x10\n\x08media_id\x18\x01 \x01(\t\x12:\n\x05state\x18\x02 \x01(\x0e\x32+.templates_stream.MediaStreamResponse.State\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12\x14\n\x0cnext_actions\x18\x04 \x03(\t\"\\\n\x05State\x12\x0b\n\x07STOPPED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0b\n\x07\x44\x45LETED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07UNKNOWN\x10\x05\x12\x07\n\x03NEW\x10\x06\x32i\n\x0bMediaStream\x12Z\n\x07\x43hanges\x12$.templates_stream.MediaStreamRequest\x1a%.templates_stream.MediaStreamResponse\"\x00\x30\x01\x62\x06proto3')
)



_MEDIASTREAMRESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='templates_stream.MediaStreamResponse.State',
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
  serialized_start=217,
  serialized_end=309,
)
_sym_db.RegisterEnumDescriptor(_MEDIASTREAMRESPONSE_STATE)


_MEDIASTREAMREQUEST = _descriptor.Descriptor(
  name='MediaStreamRequest',
  full_name='templates_stream.MediaStreamRequest',
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
  serialized_start=55,
  serialized_end=75,
)


_MEDIASTREAMRESPONSE = _descriptor.Descriptor(
  name='MediaStreamResponse',
  full_name='templates_stream.MediaStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='media_id', full_name='templates_stream.MediaStreamResponse.media_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='templates_stream.MediaStreamResponse.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='templates_stream.MediaStreamResponse.detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_actions', full_name='templates_stream.MediaStreamResponse.next_actions', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEDIASTREAMRESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=309,
)

_MEDIASTREAMRESPONSE.fields_by_name['state'].enum_type = _MEDIASTREAMRESPONSE_STATE
_MEDIASTREAMRESPONSE_STATE.containing_type = _MEDIASTREAMRESPONSE
DESCRIPTOR.message_types_by_name['MediaStreamRequest'] = _MEDIASTREAMREQUEST
DESCRIPTOR.message_types_by_name['MediaStreamResponse'] = _MEDIASTREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MediaStreamRequest = _reflection.GeneratedProtocolMessageType('MediaStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _MEDIASTREAMREQUEST,
  '__module__' : 'api.grpc.proto.media_stream_pb2'
  # @@protoc_insertion_point(class_scope:templates_stream.MediaStreamRequest)
  })
_sym_db.RegisterMessage(MediaStreamRequest)

MediaStreamResponse = _reflection.GeneratedProtocolMessageType('MediaStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _MEDIASTREAMRESPONSE,
  '__module__' : 'api.grpc.proto.media_stream_pb2'
  # @@protoc_insertion_point(class_scope:templates_stream.MediaStreamResponse)
  })
_sym_db.RegisterMessage(MediaStreamResponse)



_MEDIASTREAM = _descriptor.ServiceDescriptor(
  name='MediaStream',
  full_name='templates_stream.MediaStream',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=311,
  serialized_end=416,
  methods=[
  _descriptor.MethodDescriptor(
    name='Changes',
    full_name='templates_stream.MediaStream.Changes',
    index=0,
    containing_service=None,
    input_type=_MEDIASTREAMREQUEST,
    output_type=_MEDIASTREAMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MEDIASTREAM)

DESCRIPTOR.services_by_name['MediaStream'] = _MEDIASTREAM

# @@protoc_insertion_point(module_scope)
