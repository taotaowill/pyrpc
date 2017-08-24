# encoding: utf-8
import sys

import Echo_pb2
sys.path.append("../")
from rpc import client


def sum_callback(controller, request, response):
    if controller.Failed():
        print("Sum request failed: %s" % controller.ErrorText())
    else:
        print("Sum response: %s" % response.sum)


if __name__ == "__main__":
    chanel = client.PyRpcChannel(("127.0.0.1", 8000))

    sum_stub = Echo_pb2.SumService_Stub(chanel)
    new_controller = client.PyRpcController()
    sum_request = Echo_pb2.SumRequest()
    sum_request.nums.append(15)
    sum_request.nums.append(16)
    sum_stub.Count(new_controller, sum_request, sum_callback)

    echo_stub = Echo_pb2.EchoService_Stub(chanel)
    for i in range(5):
        controller = client.PyRpcController()
        request = Echo_pb2.EchoRequest()
        request.message = "hello world"
        response = echo_stub.Echo(controller, request)
        if not controller.Failed():
            print("Echo response: %s" % response.message)
        else:
            print("Echo request failed: %s" % controller.ErrorText())
