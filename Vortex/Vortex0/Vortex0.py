from socket import *
from struct import *

add = 0

addr = ('vortex.labs.overthewire.org', 5842)
s = socket()
s.connect(addr)

for i in range(4):
    add += unpack('<I', s.recv(4))[0]

s.send(pack('<I',add))
print(s.recv(100))
s.close()

# Username: vortex1 Password: Gq#qu3bF3
