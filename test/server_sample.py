# encoding: utf-8
import signal
import sys
import time

import Echo_pb2
sys.path.append("../")
from rpc import server
from rpc import parser

QUIT = False


def signal_handler(signum, frame):
    global QUIT
    QUIT = True


class EchoServiceImpl(Echo_pb2.EchoService):
    def Echo(self, request, response):
        response.message = request.message
        return


class SumService(Echo_pb2.SumService):
    def Count(self, request, response):
        ret = sum(request.nums)
        response.sum = ret
        return


if __name__ == "__main__":
    echo_service = EchoServiceImpl()
    sum_service = SumService()
    rpc_server = server.PyRpcServer(pro_parser_t=parser.PbParser)
    rpc_server.register_service(echo_service)
    rpc_server.register_service(sum_service)
    rpc_server.start("127.0.0.1", 8000)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    while not QUIT:
        time.sleep(1)
    print("server exit...")
    sys.exit(0)
