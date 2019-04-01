# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine/grpc/proto/engineinfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='engine/grpc/proto/engineinfo.proto',
  package='engineinfo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"engine/grpc/proto/engineinfo.proto\x12\nengineinfo\"\x16\n\x14\x45ngineIsAliveRequest\")\n\x15\x45ngineIsAliveResponse\x12\x10\n\x08is_alive\x18\x01 \x01(\x08\"\x15\n\x13\x45ngineStatusRequest\"\xed\x02\n\x14\x45ngineStatusResponse\x12\x10\n\x08is_alive\x18\x01 \x01(\x08\x12\x1b\n\x13\x62\x61\x63kground_is_alive\x18\x02 \x01(\x08\x12\x1d\n\x15\x62room_thread_is_alive\x18\x03 \x01(\x08\x12\'\n\x1f\x63hanges_domains_thread_is_alive\x18\x04 \x01(\x08\x12$\n\x1c\x63hanges_hyps_thread_is_alive\x18\x05 \x01(\x08\x12(\n download_changes_thread_is_alive\x18\x06 \x01(\x08\x12\x1d\n\x15\x65vent_thread_is_alive\x18\x07 \x01(\x08\x12\x1e\n\x16\x64isk_operations_thread\x18\x08 \x03(\t\x12\x1e\n\x16long_operations_thread\x18\t \x03(\t\x12\x17\n\x0fworking_threads\x18\n \x03(\t\x12\x16\n\x0estatus_threads\x18\x0b \x03(\t2\xb9\x01\n\nEngineInfo\x12V\n\rEngineIsAlive\x12 .engineinfo.EngineIsAliveRequest\x1a!.engineinfo.EngineIsAliveResponse\"\x00\x12S\n\x0c\x45ngineStatus\x12\x1f.engineinfo.EngineStatusRequest\x1a .engineinfo.EngineStatusResponse\"\x00\x62\x06proto3')
)




_ENGINEISALIVEREQUEST = _descriptor.Descriptor(
  name='EngineIsAliveRequest',
  full_name='engineinfo.EngineIsAliveRequest',
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
  serialized_start=50,
  serialized_end=72,
)


_ENGINEISALIVERESPONSE = _descriptor.Descriptor(
  name='EngineIsAliveResponse',
  full_name='engineinfo.EngineIsAliveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_alive', full_name='engineinfo.EngineIsAliveResponse.is_alive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=74,
  serialized_end=115,
)


_ENGINESTATUSREQUEST = _descriptor.Descriptor(
  name='EngineStatusRequest',
  full_name='engineinfo.EngineStatusRequest',
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
  serialized_start=117,
  serialized_end=138,
)


_ENGINESTATUSRESPONSE = _descriptor.Descriptor(
  name='EngineStatusResponse',
  full_name='engineinfo.EngineStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_alive', full_name='engineinfo.EngineStatusResponse.is_alive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_is_alive', full_name='engineinfo.EngineStatusResponse.background_is_alive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broom_thread_is_alive', full_name='engineinfo.EngineStatusResponse.broom_thread_is_alive', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changes_domains_thread_is_alive', full_name='engineinfo.EngineStatusResponse.changes_domains_thread_is_alive', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changes_hyps_thread_is_alive', full_name='engineinfo.EngineStatusResponse.changes_hyps_thread_is_alive', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='download_changes_thread_is_alive', full_name='engineinfo.EngineStatusResponse.download_changes_thread_is_alive', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_thread_is_alive', full_name='engineinfo.EngineStatusResponse.event_thread_is_alive', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_operations_thread', full_name='engineinfo.EngineStatusResponse.disk_operations_thread', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_operations_thread', full_name='engineinfo.EngineStatusResponse.long_operations_thread', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='working_threads', full_name='engineinfo.EngineStatusResponse.working_threads', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_threads', full_name='engineinfo.EngineStatusResponse.status_threads', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=141,
  serialized_end=506,
)

DESCRIPTOR.message_types_by_name['EngineIsAliveRequest'] = _ENGINEISALIVEREQUEST
DESCRIPTOR.message_types_by_name['EngineIsAliveResponse'] = _ENGINEISALIVERESPONSE
DESCRIPTOR.message_types_by_name['EngineStatusRequest'] = _ENGINESTATUSREQUEST
DESCRIPTOR.message_types_by_name['EngineStatusResponse'] = _ENGINESTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EngineIsAliveRequest = _reflection.GeneratedProtocolMessageType('EngineIsAliveRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENGINEISALIVEREQUEST,
  __module__ = 'engine.grpc.proto.engineinfo_pb2'
  # @@protoc_insertion_point(class_scope:engineinfo.EngineIsAliveRequest)
  ))
_sym_db.RegisterMessage(EngineIsAliveRequest)

EngineIsAliveResponse = _reflection.GeneratedProtocolMessageType('EngineIsAliveResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENGINEISALIVERESPONSE,
  __module__ = 'engine.grpc.proto.engineinfo_pb2'
  # @@protoc_insertion_point(class_scope:engineinfo.EngineIsAliveResponse)
  ))
_sym_db.RegisterMessage(EngineIsAliveResponse)

EngineStatusRequest = _reflection.GeneratedProtocolMessageType('EngineStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENGINESTATUSREQUEST,
  __module__ = 'engine.grpc.proto.engineinfo_pb2'
  # @@protoc_insertion_point(class_scope:engineinfo.EngineStatusRequest)
  ))
_sym_db.RegisterMessage(EngineStatusRequest)

EngineStatusResponse = _reflection.GeneratedProtocolMessageType('EngineStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENGINESTATUSRESPONSE,
  __module__ = 'engine.grpc.proto.engineinfo_pb2'
  # @@protoc_insertion_point(class_scope:engineinfo.EngineStatusResponse)
  ))
_sym_db.RegisterMessage(EngineStatusResponse)



_ENGINEINFO = _descriptor.ServiceDescriptor(
  name='EngineInfo',
  full_name='engineinfo.EngineInfo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=509,
  serialized_end=694,
  methods=[
  _descriptor.MethodDescriptor(
    name='EngineIsAlive',
    full_name='engineinfo.EngineInfo.EngineIsAlive',
    index=0,
    containing_service=None,
    input_type=_ENGINEISALIVEREQUEST,
    output_type=_ENGINEISALIVERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EngineStatus',
    full_name='engineinfo.EngineInfo.EngineStatus',
    index=1,
    containing_service=None,
    input_type=_ENGINESTATUSREQUEST,
    output_type=_ENGINESTATUSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENGINEINFO)

DESCRIPTOR.services_by_name['EngineInfo'] = _ENGINEINFO

# @@protoc_insertion_point(module_scope)
