from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
       IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), strict=False)
    def key_value(self):
        return

l=[]
for x in range (0, 10):
    l.append(IPv4RandomNetwork())
q=list(l)
for i in q:
    print(i)