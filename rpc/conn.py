# encoding: utf-8
"""
pyrpc connection management
"""
import asyncore
import socket
import thread


# connection
class StreamHandler(asyncore.dispatcher_with_send):
    RECV_BUFF_SIZE = 1024

    def __init__(self, sock, sock_map, parser):
        self.parser = parser
        self.parser.set_handler(self)
        asyncore.dispatcher_with_send.__init__(self, sock, map=sock_map)

    def writable(self):
        return True

    def handle_read(self):
        try:
            data = self.recv(StreamHandler.RECV_BUFF_SIZE)
            self.parser.parse(data)
        except:
            pass

    def handle_close(self):
        print("connection closed by %s" % repr(self.addr))
        self.close()

    def handle_send(self, meta, message):
        message_bytes = self.parser.serialize(meta, message)
        self.send(message_bytes)
        print("response: %s" % meta.sequence_id)


# connection manager
class StreamServer(asyncore.dispatcher):
    def __init__(self, host, port, parser):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(1024)
        self.parser = parser
        self.sock_map = {self.socket.fileno(): self}
        thread.start_new_thread(self.start_loop, ())

    def start_loop(self):
        asyncore.loop(map=self.sock_map)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print("new connection from %s" % repr(addr))
            StreamHandler(sock, self.sock_map, self.parser)
