import socket
import random

CHALLENGE_HEADER = b'\x01\x01\x01\x01'

def random_ip_address():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def run_challenge_client(dst_addr, dst_port):
    src_addr = random_ip_address()
    with socket.create_connection((dst_addr, dst_port)) as sock:
        sock.bind((src_addr, 0))
        sock.sendall(CHALLENGE_HEADER)
        sock.recv(1024)

if __name__ == "__main__":
    run_challenge_client('127.0.0.1', 12345)