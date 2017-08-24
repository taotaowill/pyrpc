# encoding: utf-8
import asyncore
import hashlib
import struct
import socket
import thread
import Queue

import google.protobuf.reflection


PYRPC_HEAD_LENGTH = 25
PYRPC_MAGIC = "^"


# pyrpc protocol parser
class ProtocolParser(object):
    HEAD = 1
    BODY = 2

    def __init__(self, handler, rpc_server):
        self.state = ProtocolParser.HEAD
        self.buff = ""
        self.body_length = 0
        self.service_index = -1
        self.method_index = -1
        self.handler = handler
        self.rpc_server = rpc_server

    def reset(self, buff):
        self.buff = buff
        self.body_length = 0
        self.state = ProtocolParser.HEAD
        self.service_index = -1
        self.method_index = -1

    def parse(self, data):
        self.buff += data
        while len(self.buff):
            if self.state == ProtocolParser.HEAD:
                if len(self.buff) < PYRPC_HEAD_LENGTH:
                    return

                try:
                    total_length, self.service_index, self.method_index, magic_str = \
                        struct.unpack("lllc", self.buff[:PYRPC_HEAD_LENGTH])
                    if magic_str != PYRPC_MAGIC:
                        print("invalid message head format, magic str mismatch!")
                        self.reset("")
                        return

                    self.body_length = total_length - PYRPC_HEAD_LENGTH
                    self.buff = self.buff[PYRPC_HEAD_LENGTH:]
                    self.state = ProtocolParser.BODY
                except Exception as e:
                    print("invalid message head format, unpack error: %s!" % e)
                    return

            if self.state == ProtocolParser.BODY:
                if len(self.buff) < self.body_length:
                    return

                body_str = self.buff[:self.body_length]
                if body_str[-1:] != PYRPC_MAGIC:
                    print("invalid message body format, magic str mismatch!")
                    self.reset(self.buff[self.body_length:])
                    return
                body_str = body_str[:-1]
                result = (self.service_index, self.method_index, body_str, self)
                self.rpc_server.run_executor.add_task(result)
                self.reset(self.buff[self.body_length:])


class StreamHandler(asyncore.dispatcher_with_send):
    def __init__(self, sock, rpc_server):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.parser = ProtocolParser(self, rpc_server)

    def handle_read(self):
        data = self.recv(5)
        self.parser.parse(data)

    def handle_close(self):
        print("connection closed by %s" % repr(self.addr))
        self.close()


# net server
class StreamServer(asyncore.dispatcher):
    def __init__(self, rpc_server, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.rpc_server = rpc_server

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print("new connection from %s" % repr(addr))
            _ = StreamHandler(sock, self.rpc_server)


# run executor
class ThreadExecutor(object):
    def __init__(self, rpc_server):
        self.rpc_server = rpc_server
        self.queue = Queue.Queue()
        for i in range(5):
            thread.start_new_thread(self.exe_task, (None,))

    def add_task(self, item):
        self.queue.put(item)

    def exe_task(self, *args, **kwargs):
        service_index, method_index, request_message_str, parser = self.queue.get()
        if service_index not in self.rpc_server.service_map:
            parser.handler.send("service not found")

        if method_index not in self.rpc_server.service_map[service_index]:
            parser.handler.send("method not found")
        method_desc, method = self.rpc_server.service_map[service_index][method_index]
        request = google.protobuf.reflection.MakeClass(method_desc.input_type)()
        request.ParseFromString(request_message_str)
        response = method(request)
        response_message_str = response.SerializeToString()
        total_bytes = 24 + len(PYRPC_MAGIC) + len(response_message_str) + len(PYRPC_MAGIC)
        f = "lll%ss" % (len(response_message_str) + 2 * len(PYRPC_MAGIC))
        ret_str = struct.pack(f, total_bytes, service_index, method_index, PYRPC_MAGIC + response_message_str + PYRPC_MAGIC)
        parser.handler.send(ret_str)


class PyRpcServer(object):
    """
    rpc server
    """
    def __init__(self):
        self.service_map = {}
        self.net_server = None
        self.run_executor = None

    @classmethod
    def unique_index(cls, string):
        return int(hashlib.sha1(string).hexdigest(), 16) % (10 ** 8)

    def register_service(self, service):
        service_index = PyRpcServer.unique_index(service.DESCRIPTOR.full_name)
        self.service_map[service_index] = {}
        for method_desc in service.DESCRIPTOR.methods:
            method = service.__getattribute__(method_desc.name)
            self.service_map[service_index][method_desc.index] = (method_desc, method)
            print "register service_index: %s, method_name: %s" % (service_index, method_desc.name)

    def start(self, host, port):
        print("server listen on %s:%s" % (host, port))
        self.run_executor = ThreadExecutor(self)
        self.net_server = StreamServer(self, host, port)
        thread.start_new_thread(lambda arg: asyncore.loop(), (None,))
