import threading
import socketserver
import socket
import contextlib
import struct

CHALLENGE_HEADER = b'\x01\x01\x01\x01'
CHALLENGE_FLAG = b'\x02\x02\x02\x02'


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class BannerTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        banner = self.server.banner
        self.request.sendall(banner.encode())

class ChallengeTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print(data[:4])
        if data[:4] == CHALLENGE_HEADER:
            print("Magic val sent")
            self.request.sendall(CHALLENGE_HEADER + CHALLENGE_FLAG)

def start_server(port, banner):
    if port == 12345:
        server = ThreadingTCPServer(('0.0.0.0', port), ChallengeTCPHandler)
    else:
        server = ThreadingTCPServer(('0.0.0.0', port), BannerTCPHandler)

    server.banner = banner
    server.serve_forever()

if __name__ == "__main__":
    banners = {
        12345: "Welcome to port 12345!\n",
        80: "Welcome to port 80!\n",
        8080: "Welcome to port 8080!\n",
        8081: "Welcome to port 8081!\n",
        # ...
        8199: "Welcome to port 8199!\n",
    }
    for port, banner in banners.items():
        print(f"Starting server on port {port} : {banner}")
        t = threading.Thread(target=start_server, args=(port, banner))
        t.start()
