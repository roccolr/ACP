# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hellosalerno.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12hellosalerno.proto\x12\x13hellosalerno_duplex\"\x1c\n\x0chelloRequest\x12\x0c\n\x04nome\x18\x01 \x01(\t\"\x19\n\nhelloReply\x12\x0b\n\x03msg\x18\x01 \x01(\t2_\n\x07Greeter\x12T\n\x08sayHello\x12!.hellosalerno_duplex.helloRequest\x1a\x1f.hellosalerno_duplex.helloReply\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hellosalerno_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLOREQUEST']._serialized_start=43
  _globals['_HELLOREQUEST']._serialized_end=71
  _globals['_HELLOREPLY']._serialized_start=73
  _globals['_HELLOREPLY']._serialized_end=98
  _globals['_GREETER']._serialized_start=100
  _globals['_GREETER']._serialized_end=195
# @@protoc_insertion_point(module_scope)
