# encoding: utf-8
"""
pyrpc protocol parser
"""
import struct

from . import meta_pb2


class IParser(object):
    def __init__(self):
        self.handler = None

    def set_handler(self, handler):
        self.handler = handler

    def parse(self, data):
        raise NotImplementedError

    def serialize(self, *args, **kwargs):
        raise NotImplementedError


class PbParser(IParser):
    HEADER_SIZE = 25
    MAGIC_STR = "PYRPC"
    STATE_HEAD = 1
    STATE_BODY = 2

    def __init__(self, on_parse=None, on_error=None):
        IParser.__init__(self)
        self.on_parse = on_parse
        self.on_error = on_error
        self.state = PbParser.STATE_HEAD
        self.buff = ""
        self.meta_size = 0
        self.message_size = 0

    def reset(self, buff):
        self.state = PbParser.STATE_HEAD
        self.buff = buff
        self.meta_size = 0
        self.message_size = 0

    def parse(self, data):
        self.buff += data
        ret = []
        while len(self.buff):
            if self.state == PbParser.STATE_HEAD:
                if len(self.buff) < PbParser.HEADER_SIZE:
                    break

                try:
                    magic_str, meta_size, message_size, body_size = \
                        struct.unpack("<5siqq", self.buff[:PbParser.HEADER_SIZE])
                    if magic_str != PbParser.MAGIC_STR:
                        print("invalid message head format, magic str mismatch!")
                        self.reset("")
                        break
                    if body_size != meta_size + message_size:
                        print("invalid message head format, meta_size + message_size != body_size!")
                        self.reset("")
                        break

                    self.meta_size = meta_size
                    self.message_size = message_size
                    self.state = PbParser.STATE_BODY
                except Exception as e:
                    print("invalid message head format, unpack error: %s!" % e)
                    break

            if self.state == PbParser.STATE_BODY:
                if len(self.buff) < PbParser.HEADER_SIZE + self.meta_size + self.message_size:
                    break

                meta = meta_pb2.RpcMeta()
                meta_start = PbParser.HEADER_SIZE
                meta.ParseFromString(self.buff[meta_start: meta_start + self.meta_size])
                message_start = meta_start + self.meta_size
                message_str = self.buff[message_start: message_start + self.message_size]
                ret.append((meta, message_str, self.handler))
                if self.on_parse:
                    self.on_parse((meta, message_str, self.handler))
                self.reset(self.buff[message_start + self.message_size:])

        return ret

    @classmethod
    def serialize(cls, meta, message):
        meta_str = meta.SerializeToString()
        message_str = ""
        if message:
            message_str = message.SerializeToString()
        meta_size = len(meta_str)
        message_size = len(message_str)
        body_size = meta_size + message_size
        return struct.pack("<5siqq%ss" % body_size, PbParser.MAGIC_STR,
                           meta_size, message_size, body_size, meta_str + message_str)
