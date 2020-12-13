# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: batlshm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='batlshm.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbatlshm.proto\"\x07\n\x05\x45mpty\"\x1f\n\rStandardReply\x12\x0e\n\x06result\x18\x01 \x01(\x05\"#\n\x13\x43reateBufferRequest\x12\x0c\n\x04size\x18\x01 \x01(\x05\"1\n\x11\x43reateBufferReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x05\" \n\x10GetBufferRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\".\n\x0eGetBufferReply\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0c\n\x04size\x18\x02 \x01(\r\"$\n\x14ReleaseBufferRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x14RegisterTopicRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"L\n\x0ePublishRequest\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x13\n\x0b\x62uffer_name\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"\x1d\n\x0fGenerateIDReply\x12\n\n\x02id\x18\x01 \x01(\r\"2\n\x10SubscribeRequest\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"-\n\x0bPullRequest\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"C\n\tPullReply\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x13\n\x0b\x62uffer_name\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x32\x9a\x03\n\x07\x42\x61tlShm\x12:\n\x0c\x43reateBuffer\x12\x14.CreateBufferRequest\x1a\x12.CreateBufferReply\"\x00\x12\x31\n\tGetBuffer\x12\x11.GetBufferRequest\x1a\x0f.GetBufferReply\"\x00\x12\x38\n\rReleaseBuffer\x12\x15.ReleaseBufferRequest\x1a\x0e.StandardReply\"\x00\x12\x38\n\rRegisterTopic\x12\x15.RegisterTopicRequest\x1a\x0e.StandardReply\"\x00\x12,\n\x07Publish\x12\x0f.PublishRequest\x1a\x0e.StandardReply\"\x00\x12(\n\nGenerateID\x12\x06.Empty\x1a\x10.GenerateIDReply\"\x00\x12\x30\n\tSubscribe\x12\x11.SubscribeRequest\x1a\x0e.StandardReply\"\x00\x12\"\n\x04Pull\x12\x0c.PullRequest\x1a\n.PullReply\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=17,
  serialized_end=24,
)


_STANDARDREPLY = _descriptor.Descriptor(
  name='StandardReply',
  full_name='StandardReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='StandardReply.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=57,
)


_CREATEBUFFERREQUEST = _descriptor.Descriptor(
  name='CreateBufferRequest',
  full_name='CreateBufferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='CreateBufferRequest.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=59,
  serialized_end=94,
)


_CREATEBUFFERREPLY = _descriptor.Descriptor(
  name='CreateBufferReply',
  full_name='CreateBufferReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateBufferReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='CreateBufferReply.result', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=96,
  serialized_end=145,
)


_GETBUFFERREQUEST = _descriptor.Descriptor(
  name='GetBufferRequest',
  full_name='GetBufferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='GetBufferRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=147,
  serialized_end=179,
)


_GETBUFFERREPLY = _descriptor.Descriptor(
  name='GetBufferReply',
  full_name='GetBufferReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GetBufferReply.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='GetBufferReply.size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=181,
  serialized_end=227,
)


_RELEASEBUFFERREQUEST = _descriptor.Descriptor(
  name='ReleaseBufferRequest',
  full_name='ReleaseBufferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ReleaseBufferRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=229,
  serialized_end=265,
)


_REGISTERTOPICREQUEST = _descriptor.Descriptor(
  name='RegisterTopicRequest',
  full_name='RegisterTopicRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RegisterTopicRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=267,
  serialized_end=303,
)


_PUBLISHREQUEST = _descriptor.Descriptor(
  name='PublishRequest',
  full_name='PublishRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='PublishRequest.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffer_name', full_name='PublishRequest.buffer_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PublishRequest.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=305,
  serialized_end=381,
)


_GENERATEIDREPLY = _descriptor.Descriptor(
  name='GenerateIDReply',
  full_name='GenerateIDReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GenerateIDReply.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=383,
  serialized_end=412,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='SubscribeRequest.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='SubscribeRequest.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=414,
  serialized_end=464,
)


_PULLREQUEST = _descriptor.Descriptor(
  name='PullRequest',
  full_name='PullRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='PullRequest.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='PullRequest.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=466,
  serialized_end=511,
)


_PULLREPLY = _descriptor.Descriptor(
  name='PullReply',
  full_name='PullReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='PullReply.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffer_name', full_name='PullReply.buffer_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PullReply.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=513,
  serialized_end=580,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['StandardReply'] = _STANDARDREPLY
DESCRIPTOR.message_types_by_name['CreateBufferRequest'] = _CREATEBUFFERREQUEST
DESCRIPTOR.message_types_by_name['CreateBufferReply'] = _CREATEBUFFERREPLY
DESCRIPTOR.message_types_by_name['GetBufferRequest'] = _GETBUFFERREQUEST
DESCRIPTOR.message_types_by_name['GetBufferReply'] = _GETBUFFERREPLY
DESCRIPTOR.message_types_by_name['ReleaseBufferRequest'] = _RELEASEBUFFERREQUEST
DESCRIPTOR.message_types_by_name['RegisterTopicRequest'] = _REGISTERTOPICREQUEST
DESCRIPTOR.message_types_by_name['PublishRequest'] = _PUBLISHREQUEST
DESCRIPTOR.message_types_by_name['GenerateIDReply'] = _GENERATEIDREPLY
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['PullRequest'] = _PULLREQUEST
DESCRIPTOR.message_types_by_name['PullReply'] = _PULLREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

StandardReply = _reflection.GeneratedProtocolMessageType('StandardReply', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDREPLY,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:StandardReply)
  })
_sym_db.RegisterMessage(StandardReply)

CreateBufferRequest = _reflection.GeneratedProtocolMessageType('CreateBufferRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBUFFERREQUEST,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:CreateBufferRequest)
  })
_sym_db.RegisterMessage(CreateBufferRequest)

CreateBufferReply = _reflection.GeneratedProtocolMessageType('CreateBufferReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBUFFERREPLY,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:CreateBufferReply)
  })
_sym_db.RegisterMessage(CreateBufferReply)

GetBufferRequest = _reflection.GeneratedProtocolMessageType('GetBufferRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUFFERREQUEST,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:GetBufferRequest)
  })
_sym_db.RegisterMessage(GetBufferRequest)

GetBufferReply = _reflection.GeneratedProtocolMessageType('GetBufferReply', (_message.Message,), {
  'DESCRIPTOR' : _GETBUFFERREPLY,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:GetBufferReply)
  })
_sym_db.RegisterMessage(GetBufferReply)

ReleaseBufferRequest = _reflection.GeneratedProtocolMessageType('ReleaseBufferRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEBUFFERREQUEST,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:ReleaseBufferRequest)
  })
_sym_db.RegisterMessage(ReleaseBufferRequest)

RegisterTopicRequest = _reflection.GeneratedProtocolMessageType('RegisterTopicRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTOPICREQUEST,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:RegisterTopicRequest)
  })
_sym_db.RegisterMessage(RegisterTopicRequest)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)

GenerateIDReply = _reflection.GeneratedProtocolMessageType('GenerateIDReply', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEIDREPLY,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:GenerateIDReply)
  })
_sym_db.RegisterMessage(GenerateIDReply)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

PullRequest = _reflection.GeneratedProtocolMessageType('PullRequest', (_message.Message,), {
  'DESCRIPTOR' : _PULLREQUEST,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:PullRequest)
  })
_sym_db.RegisterMessage(PullRequest)

PullReply = _reflection.GeneratedProtocolMessageType('PullReply', (_message.Message,), {
  'DESCRIPTOR' : _PULLREPLY,
  '__module__' : 'batlshm_pb2'
  # @@protoc_insertion_point(class_scope:PullReply)
  })
_sym_db.RegisterMessage(PullReply)



_BATLSHM = _descriptor.ServiceDescriptor(
  name='BatlShm',
  full_name='BatlShm',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=583,
  serialized_end=993,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBuffer',
    full_name='BatlShm.CreateBuffer',
    index=0,
    containing_service=None,
    input_type=_CREATEBUFFERREQUEST,
    output_type=_CREATEBUFFERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBuffer',
    full_name='BatlShm.GetBuffer',
    index=1,
    containing_service=None,
    input_type=_GETBUFFERREQUEST,
    output_type=_GETBUFFERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReleaseBuffer',
    full_name='BatlShm.ReleaseBuffer',
    index=2,
    containing_service=None,
    input_type=_RELEASEBUFFERREQUEST,
    output_type=_STANDARDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterTopic',
    full_name='BatlShm.RegisterTopic',
    index=3,
    containing_service=None,
    input_type=_REGISTERTOPICREQUEST,
    output_type=_STANDARDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='BatlShm.Publish',
    index=4,
    containing_service=None,
    input_type=_PUBLISHREQUEST,
    output_type=_STANDARDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateID',
    full_name='BatlShm.GenerateID',
    index=5,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_GENERATEIDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='BatlShm.Subscribe',
    index=6,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_STANDARDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Pull',
    full_name='BatlShm.Pull',
    index=7,
    containing_service=None,
    input_type=_PULLREQUEST,
    output_type=_PULLREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BATLSHM)

DESCRIPTOR.services_by_name['BatlShm'] = _BATLSHM

# @@protoc_insertion_point(module_scope)