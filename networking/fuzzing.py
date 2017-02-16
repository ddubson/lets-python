# https://www.owasp.org/index.php/Fuzzing

from pyfuzz.generator import random_ascii
import socket

msg = random_ascii() + b" / HTTP/1.1\nHost: localhost\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(msg)

try:
    addr = ("localhost", 80)
    s.connect(addr)
    s.sendall(msg)
    resp = s.recv(4096)
    print(resp)
except Exception as e:
    print(e)
finally:
    s.close()
