import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port number to spoof
spoofed_ip = '172.25.30.40'
port = 12345

# Set the destination IP and port
destination_ip = '172.25.30.153'

# Set the packet data
data = b'\x01\x02\x03\x04'

# Set the socket options to allow spoofing the IP address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_DONTROUTE, 1)
s.setsockopt(socket.SOL_IP, socket.IP_TRANSPARENT, 1)
s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)

# Bind the socket to the spoofed IP and port
s.bind((spoofed_ip, port))

# Connect to the destination IP and port
s.connect((destination_ip, port))

# Send the packet data
s.send(data)

# Close the socket
s.close()