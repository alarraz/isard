# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='engine.proto',
  package='engine',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x65ngine.proto\x12\x06\x65ngine\"\x16\n\x08\x64omainID\x12\n\n\x02id\x18\x01 \x01(\t\"\xd1\x01\n\x18\x64omainCreateFromTemplate\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x13\n\x0btemplate_id\x18\x02 \x01(\t\x1a\x8c\x01\n\x08hardware\x12\r\n\x05vcpus\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x05\x12\x0e\n\x06videos\x18\x03 \x03(\t\x12\x0c\n\x04\x62oot\x18\x04 \x03(\t\x12\x12\n\ninterfaces\x18\x05 \x03(\t\x12\x0f\n\x07\x64iskbus\x18\x06 \x01(\t\x12\x0c\n\x04isos\x18\x07 \x03(\t\x12\x10\n\x08\x66loppies\x18\x08 \x03(\t\"\xd1\x01\n\x18templateCreateFromDomain\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x13\n\x0btemplate_id\x18\x02 \x01(\t\x1a\x8c\x01\n\x08hardware\x12\r\n\x05vcpus\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x05\x12\x0e\n\x06videos\x18\x03 \x03(\t\x12\x0c\n\x04\x62oot\x18\x04 \x03(\t\x12\x12\n\ninterfaces\x18\x05 \x03(\t\x12\x0f\n\x07\x64iskbus\x18\x06 \x01(\t\x12\x0c\n\x04isos\x18\x07 \x03(\t\x12\x10\n\x08\x66loppies\x18\x08 \x03(\t\"\x1e\n\x0c\x61\x63tionResult\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32\xdf\x02\n\x06\x45ngine\x12\x37\n\x0b\x44omainStart\x12\x10.engine.domainID\x1a\x14.engine.actionResult\"\x00\x12\x36\n\nDomainStop\x12\x10.engine.domainID\x1a\x14.engine.actionResult\"\x00\x12\x38\n\x0c\x44omainDelete\x12\x10.engine.domainID\x1a\x14.engine.actionResult\"\x00\x12T\n\x18\x44omainCreateFromTemplate\x12 .engine.domainCreateFromTemplate\x1a\x14.engine.actionResult\"\x00\x12T\n\x18TemplateCreateFromDomain\x12 .engine.templateCreateFromDomain\x1a\x14.engine.actionResult\"\x00\x62\x06proto3')
)




_DOMAINID = _descriptor.Descriptor(
  name='domainID',
  full_name='engine.domainID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='engine.domainID.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=24,
  serialized_end=46,
)


_DOMAINCREATEFROMTEMPLATE_HARDWARE = _descriptor.Descriptor(
  name='hardware',
  full_name='engine.domainCreateFromTemplate.hardware',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vcpus', full_name='engine.domainCreateFromTemplate.hardware.vcpus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='engine.domainCreateFromTemplate.hardware.memory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videos', full_name='engine.domainCreateFromTemplate.hardware.videos', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot', full_name='engine.domainCreateFromTemplate.hardware.boot', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaces', full_name='engine.domainCreateFromTemplate.hardware.interfaces', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diskbus', full_name='engine.domainCreateFromTemplate.hardware.diskbus', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isos', full_name='engine.domainCreateFromTemplate.hardware.isos', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floppies', full_name='engine.domainCreateFromTemplate.hardware.floppies', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=118,
  serialized_end=258,
)

_DOMAINCREATEFROMTEMPLATE = _descriptor.Descriptor(
  name='domainCreateFromTemplate',
  full_name='engine.domainCreateFromTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='engine.domainCreateFromTemplate.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='engine.domainCreateFromTemplate.template_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DOMAINCREATEFROMTEMPLATE_HARDWARE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=258,
)


_TEMPLATECREATEFROMDOMAIN_HARDWARE = _descriptor.Descriptor(
  name='hardware',
  full_name='engine.templateCreateFromDomain.hardware',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vcpus', full_name='engine.templateCreateFromDomain.hardware.vcpus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='engine.templateCreateFromDomain.hardware.memory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videos', full_name='engine.templateCreateFromDomain.hardware.videos', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot', full_name='engine.templateCreateFromDomain.hardware.boot', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaces', full_name='engine.templateCreateFromDomain.hardware.interfaces', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diskbus', full_name='engine.templateCreateFromDomain.hardware.diskbus', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isos', full_name='engine.templateCreateFromDomain.hardware.isos', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floppies', full_name='engine.templateCreateFromDomain.hardware.floppies', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=118,
  serialized_end=258,
)

_TEMPLATECREATEFROMDOMAIN = _descriptor.Descriptor(
  name='templateCreateFromDomain',
  full_name='engine.templateCreateFromDomain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='engine.templateCreateFromDomain.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='engine.templateCreateFromDomain.template_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TEMPLATECREATEFROMDOMAIN_HARDWARE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=470,
)


_ACTIONRESULT = _descriptor.Descriptor(
  name='actionResult',
  full_name='engine.actionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='engine.actionResult.result', index=0,
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
  serialized_start=472,
  serialized_end=502,
)

_DOMAINCREATEFROMTEMPLATE_HARDWARE.containing_type = _DOMAINCREATEFROMTEMPLATE
_TEMPLATECREATEFROMDOMAIN_HARDWARE.containing_type = _TEMPLATECREATEFROMDOMAIN
DESCRIPTOR.message_types_by_name['domainID'] = _DOMAINID
DESCRIPTOR.message_types_by_name['domainCreateFromTemplate'] = _DOMAINCREATEFROMTEMPLATE
DESCRIPTOR.message_types_by_name['templateCreateFromDomain'] = _TEMPLATECREATEFROMDOMAIN
DESCRIPTOR.message_types_by_name['actionResult'] = _ACTIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

domainID = _reflection.GeneratedProtocolMessageType('domainID', (_message.Message,), dict(
  DESCRIPTOR = _DOMAINID,
  __module__ = 'engine_pb2'
  # @@protoc_insertion_point(class_scope:engine.domainID)
  ))
_sym_db.RegisterMessage(domainID)

domainCreateFromTemplate = _reflection.GeneratedProtocolMessageType('domainCreateFromTemplate', (_message.Message,), dict(

  hardware = _reflection.GeneratedProtocolMessageType('hardware', (_message.Message,), dict(
    DESCRIPTOR = _DOMAINCREATEFROMTEMPLATE_HARDWARE,
    __module__ = 'engine_pb2'
    # @@protoc_insertion_point(class_scope:engine.domainCreateFromTemplate.hardware)
    ))
  ,
  DESCRIPTOR = _DOMAINCREATEFROMTEMPLATE,
  __module__ = 'engine_pb2'
  # @@protoc_insertion_point(class_scope:engine.domainCreateFromTemplate)
  ))
_sym_db.RegisterMessage(domainCreateFromTemplate)
_sym_db.RegisterMessage(domainCreateFromTemplate.hardware)

templateCreateFromDomain = _reflection.GeneratedProtocolMessageType('templateCreateFromDomain', (_message.Message,), dict(

  hardware = _reflection.GeneratedProtocolMessageType('hardware', (_message.Message,), dict(
    DESCRIPTOR = _TEMPLATECREATEFROMDOMAIN_HARDWARE,
    __module__ = 'engine_pb2'
    # @@protoc_insertion_point(class_scope:engine.templateCreateFromDomain.hardware)
    ))
  ,
  DESCRIPTOR = _TEMPLATECREATEFROMDOMAIN,
  __module__ = 'engine_pb2'
  # @@protoc_insertion_point(class_scope:engine.templateCreateFromDomain)
  ))
_sym_db.RegisterMessage(templateCreateFromDomain)
_sym_db.RegisterMessage(templateCreateFromDomain.hardware)

actionResult = _reflection.GeneratedProtocolMessageType('actionResult', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONRESULT,
  __module__ = 'engine_pb2'
  # @@protoc_insertion_point(class_scope:engine.actionResult)
  ))
_sym_db.RegisterMessage(actionResult)



_ENGINE = _descriptor.ServiceDescriptor(
  name='Engine',
  full_name='engine.Engine',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=505,
  serialized_end=856,
  methods=[
  _descriptor.MethodDescriptor(
    name='DomainStart',
    full_name='engine.Engine.DomainStart',
    index=0,
    containing_service=None,
    input_type=_DOMAINID,
    output_type=_ACTIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DomainStop',
    full_name='engine.Engine.DomainStop',
    index=1,
    containing_service=None,
    input_type=_DOMAINID,
    output_type=_ACTIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DomainDelete',
    full_name='engine.Engine.DomainDelete',
    index=2,
    containing_service=None,
    input_type=_DOMAINID,
    output_type=_ACTIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DomainCreateFromTemplate',
    full_name='engine.Engine.DomainCreateFromTemplate',
    index=3,
    containing_service=None,
    input_type=_DOMAINCREATEFROMTEMPLATE,
    output_type=_ACTIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TemplateCreateFromDomain',
    full_name='engine.Engine.TemplateCreateFromDomain',
    index=4,
    containing_service=None,
    input_type=_TEMPLATECREATEFROMDOMAIN,
    output_type=_ACTIONRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENGINE)

DESCRIPTOR.services_by_name['Engine'] = _ENGINE

# @@protoc_insertion_point(module_scope)
