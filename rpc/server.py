# encoding: utf-8
"""
pyrpc server implement
"""
import thread
import Queue

import google.protobuf.reflection

from . import conn
from . import parser
from . import meta_pb2


class RunExecutor(object):
    """method executor"""
    def __init__(self, method_map, queue, threads=8):
        self.method_map = method_map
        self.queue = queue
        for i in range(threads):
            thread.start_new_thread(self.exe_task, (None,))

    def exe_task(self, _):
        while True:
            req_meta, req_message_str, conn_handler = self.queue.get()
            res_meta = meta_pb2.RpcMeta()
            res_meta.sequence_id = req_meta.sequence_id

            if req_meta.method not in self.method_map:
                res_meta.failed = True
                res_meta.error_code = 1
                res_meta.error_text = "method does not exist"
                conn_handler.handle_send(res_meta, None)
                return

            method_desc, method = self.method_map[req_meta.method]
            try:
                request = google.protobuf.reflection.MakeClass(method_desc.input_type)()
                request.ParseFromString(req_message_str)
                response = google.protobuf.reflection.MakeClass(method_desc.output_type)()
                method(request, response)
                conn_handler.handle_send(res_meta, response)
            except Exception as e:
                res_meta.failed = True
                res_meta.error_code = 1
                res_meta.error_text = "execute method failed, error: %s" % e
                conn_handler.handle_send(res_meta, None)
                return


class PyRpcServer(object):
    """rpc server"""
    def __init__(self, threads=8, max_requests=1024, pro_parser_t=None, net_server_t=None):
        self.threads = threads
        self.max_requests = max_requests
        self.pro_parser_t = pro_parser_t or parser.PbParser
        self.net_server_t = net_server_t or conn.StreamServer

        self.queue = Queue.Queue(self.max_requests)
        self.method_map = {}
        self.net_server = None
        self.run_executor = None

    def register_service(self, service):
        for method_desc in service.DESCRIPTOR.methods:
            method = service.__getattribute__(method_desc.name)
            self.method_map[method_desc.full_name] = (method_desc, method)
            print "register method: %s" % method_desc.full_name

    def start(self, host, port):
        print("server listen on %s:%s" % (host, port))
        self.run_executor = RunExecutor(self.method_map, self.queue, self.threads)
        parent = self

        # start net server
        pro_parser = self.pro_parser_t()
        pro_parser.on_parse = lambda message: parent.queue.put(message)
        self.net_server = self.net_server_t(host, port, pro_parser)
