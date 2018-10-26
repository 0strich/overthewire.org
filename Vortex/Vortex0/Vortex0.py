from socket import *
from struct import *

host = 'vortex.labs.overthewire.org'
port = 5842
add = 0
conn=(host,port)

s = socket()
s.connect(conn)
for i in range(4):
	add += unpack('<I',s.recv(4))[0]

s.send(pack('<I',add))
print(s.recv(100))
s.close()

# Username: vortex1 Password: Gq#qu3bF3
# test version
