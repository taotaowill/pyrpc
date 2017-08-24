# encoding: utf-8
import socket

import Echo_pb2
from rpc import meta_pb2
from rpc import parser


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect(("127.0.0.1", 8000))

    meta = meta_pb2.RpcMeta()
    meta.sequence_id = str(0)
    meta.method = "pyrpc.test.EchoService.Echo"
    request = Echo_pb2.EchoRequest()
    request.message = "hello world"

    pb_parser = parser.PbParser()
    req_bytes = pb_parser.serialize(meta, request)

    sock.send(req_bytes[:2])
    sock.send(req_bytes[2:])

    res_bytes = sock.recv(1024)
    response = Echo_pb2.EchoResponse()
    res_list = pb_parser.parse(res_bytes)
    response.ParseFromString(res_list[0][1])
    print response.message