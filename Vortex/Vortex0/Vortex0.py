from socket import *
from struct import pack, unpack

add = 0

addr = ('vortex.labs.overthewire.org', 5842)
s = socket()
s.connect(addr)

while(True):
    try:
        for i in range(4):
            add += unpack('<I', s.recv(4))[0]

        s.send(pack('<I',add))
        print(s.recv(100))
        break
    except:
        continue

s.close()

# Username: vortex1 Password: Gq#qu3bF3
