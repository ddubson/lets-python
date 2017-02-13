# complimentary command
# nc -l -p 5599 --udp localhost

import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b"Hi this is a message", ("localhost", 5599))
except Exception as e:
    print("Except: ", e)
finally:
    print("Sent the message")