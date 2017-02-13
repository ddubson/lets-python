# Execute in sudo to send raw TCP/IP Packet

from scapy.all import *
from scapy.layers.inet import TCP, IP

macAddr = "15:16:89:fa:dd:09"
ipAddr = "9.16.5.4"
payload = "This is the payload"

# Create a TCP/IP Packet
frame = Ether(dst=macAddr)/IP(dst=ipAddr)/TCP()/payload

print(frame)
sendp(frame)
