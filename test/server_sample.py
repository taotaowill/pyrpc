# encoding: utf-8
import signal
import sys
import time

sys.path.append("../")

import Echo_pb2
from rpc import server

QUIT = False


def signal_handler(signum, frame):
    global QUIT
    QUIT = True


class EchoServiceImpl(Echo_pb2.EchoService):
    def Echo(self, request):
        print("request message: %s" % request.message)
        response = Echo_pb2.EchoResponse()
        response.message = request.message
        return response


if __name__ == "__main__":
    echo_service = EchoServiceImpl()
    rpc_server = server.PyRpcServer()
    rpc_server.register_service(echo_service)
    rpc_server.start("127.0.0.1", 8080)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    while not QUIT:
        time.sleep(1)
    print("server exit...")
    sys.exit(0)
