# encoding: utf-8
"""
pyrpc client implement
"""
import asyncore
import socket
import time
import thread
import threading

import google.protobuf.service

from . import conn
from . import parser
from . import meta_pb2

sock_map = {}


def forever_loop():
    while True:
        asyncore.loop(map=sock_map, count=1)

thread.start_new_thread(forever_loop, ())


class PyRpcController(google.protobuf.service.RpcController):
    def __init__(self):
        self.done = False
        self.error_code = 0
        self.error_text = ""
        self.callback = None
        self.response = None

    def Reset(self):
        self.done = False
        self.error_code = 0
        self.error_text = ""
        self.response = None

    def Failed(self):
        return 0 != self.error_code

    def ErrorText(self):
        return self.error_text

    def StartCancel(self):
        pass

    def SetFailed(self, reason):
        self.error_code = -1
        self.error_text = reason
        self.done = True

    def IsCanceled(self):
        pass

    def NotifyOnCancel(self, callback):
        pass

    def SetSuccess(self, response):
        self.error_code = 0
        self.response = response
        self.done = True

    def IsDone(self):
        return self.done

    def GetResponse(self):
        return self.response


class PyRpcChannel(google.protobuf.service.RpcChannel):
    def __init__(self, addr):
        self.addr = addr
        self.sequence_id = 0
        self.lock = threading.Lock()
        self.conn = None
        self.pb_parser = parser.PbParser()
        self.pb_parser.on_parse = self.on_parse
        self.controller_map = {}

    def on_parse(self, raw_message):
        res_meta, res_message_str, _ = raw_message
        rpc_controller = self.controller_map.pop(res_meta.sequence_id, None)
        if not rpc_controller:
            return

        if res_meta.error_code != 0:
            rpc_controller.SetFailed(res_meta.error_code, res_meta.error_text)
            return

        response = rpc_controller.response_class()
        response.ParseFromString(res_message_str)
        rpc_controller.SetSuccess(response)
        if rpc_controller.callback:
            rpc_controller.callback(rpc_controller, rpc_controller.request, response)

    def get_sequence_id(self):
        self.lock.acquire()
        self.sequence_id += 1
        self.lock.release()
        return str(self.sequence_id)

    def CallMethod(self, method_descriptor, rpc_controller, request, response_class, done):
        if self.conn is None:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect(self.addr)
                self.conn = conn.StreamHandler(sock, sock_map, self.pb_parser)
            except socket.error as e:
                rpc_controller.SetFailed("socket connect failed, %s" % e)
                return

        req_meta = meta_pb2.RpcMeta()
        req_meta.sequence_id = str(self.get_sequence_id())
        rpc_controller.request = request
        rpc_controller.response_class = response_class
        rpc_controller.callback = done
        self.controller_map[req_meta.sequence_id] = rpc_controller
        req_meta.method = method_descriptor.full_name
        request_bytes = self.pb_parser.serialize(req_meta, request)
        self.conn.send(request_bytes)

        if done:
            return

        while not rpc_controller.IsDone():
            time.sleep(0.1)

        if rpc_controller.Failed():
            return None

        return rpc_controller.GetResponse()
