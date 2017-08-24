# encoding: utf-8
import sys
import socket
import struct
import hashlib

import Echo_pb2


def unique_index(string):
    return int(hashlib.sha1(string).hexdigest(), 16) % (10 ** 8)


def encode_request(req):
    body_str = "^" + req.SerializeToString() + "^"
    total_bytes = len(body_str) + 24
    f = "lll%ss" % len(body_str)
    service_index = unique_index(Echo_pb2.EchoService.DESCRIPTOR.full_name)
    return struct.pack(f, total_bytes, service_index, 0, body_str)


def decode_response(res_bytes, res):
    total_bytes, service_index, method_index, magic_str = struct.unpack("lllc", res_bytes[:25])
    body_bytes = total_bytes - 26
    f = "%ssc" % body_bytes
    body_str, magic_str = struct.unpack(f, res_bytes[25:total_bytes])
    res.ParseFromString(body_str)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 8080))
    request = Echo_pb2.EchoRequest()
    request.message = "hello world"
    req_bytes = encode_request(request)
    sock.send(req_bytes)
    res_bytes = sock.recv(1024)
    response = Echo_pb2.EchoResponse()
    decode_response(res_bytes, response)
    print response.message
