import ssl
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(socket)

try:
    ssl_socket.connect(("www.google.com", 443))
    print(ssl_socket.cipher())
except:
    print("error")

try:
    ssl_socket.write(b"GET / HTTP/1.1\r\n")
    ssl_socket.write(b"Host: www.google.com\n\n")
except Exception as e:
    print("write error: ", e)

data = bytearray()
try:
    data = ssl_socket.read()
except Exception as e:
    print("read error: ", e)

print(data.decode("utf-8"))
