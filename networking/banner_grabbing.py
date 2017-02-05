import socket
import re

host = "www.microsoft.com"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

http_get = b"GET / HTTP/1.1\nHost:www.microsoft.com\n\n"
data = ''
try:
    sock.sendall(http_get)
    data = sock.recvfrom(1024)
except socket.error:
    print("Socket error", socket.errno)
finally:
    print("closing connection")
    sock.close()

strdata = data[0].decode("utf-8")

headers = strdata.splitlines()

for s in headers:
    if re.search('Server:', s):
        s = s.replace("Server: ", "")
        print(s)
