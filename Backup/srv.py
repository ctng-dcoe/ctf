import socket
import contextlib
import struct

import socketserver

CHALLENGE_HEADER = b'\x01\x01\x01\x01'
CHALLENGE_FLAG = b'\x02\x02\x02\x02'

class ChallengeTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print(data[:4])
        if data[:4] == CHALLENGE_HEADER:
            print("Magic val sent")
            self.request.sendall(CHALLENGE_HEADER + CHALLENGE_FLAG)

def run_challenge_server():
    server = socketserver.TCPServer(('0.0.0.0', 12345), ChallengeTCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    run_challenge_server()
