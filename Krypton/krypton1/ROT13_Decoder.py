Encrypted = 'YRIRY GJB CNFFJBEQ EBGGRA'
ROT13_Decoder = ''
remainder = 0

for i in Encrypted:
	if(ord(i) >= ord('A') and ord(i) <= ord('Z')):
		if(ord(i) + 13 <= ord('Z')):
			ROT13_Decoder += chr(ord(i) + 13)
		else:
			remainder = 12 - (ord('Z') - ord(i))
			ROT13_Decoder += chr(ord('A') + remainder)
	else: ROT13_Decoder += i

print(ROT13_Decoder)

# LEVEL TWO PASSWORD ROTTEN
