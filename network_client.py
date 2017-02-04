# To test run netcat: `nc -p 5555 -l`

import socket

host = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (host, 5555)
sock.connect(addr)

try:
    msg = b"hi, this is a test\n"
    sock.sendall(msg)
except socket.errno:
    print("socket error")
finally:
    sock.close()
