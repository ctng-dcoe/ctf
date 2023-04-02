import socket

# The magic value to send to the server
MAGIC_VALUE = b'abc123'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 10000)
print('connecting to', server_address)
sock.connect(server_address)

try:
    # Send the magic value to the server
    sock.sendall(MAGIC_VALUE)

    # Look for the response from the server
    amount_received = 0
    amount_expected = len(MAGIC_VALUE)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    # Clean up the connection
    sock.close()