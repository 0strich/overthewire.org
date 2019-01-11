from string import *

enc = 'YRIRY GJB CNFFJBEQ EBGGRA'

before = ''.join([chr(i) for i in range(65,91)])
after = before[13:] + before[:13]
string = maketrans(before, after)

print(enc.translate(string))

# LEVEL TWO PASSWORD ROTTEN
