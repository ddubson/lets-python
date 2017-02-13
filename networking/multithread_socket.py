import socket
import threading


class ClientConnect(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = ("www.google.com", 443)
        sock.connect(addr)
        print("Connected")


sockClients = []
for i in range(1, 10):
    s = ClientConnect()
    s.start()
    print("started ", i)
    sockClients.append(s)
