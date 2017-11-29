string = 'Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'
decode = ''
remainder = 0

for i in string:
	if(ord(i) >= ord('a') and ord(i) <= ord('z')):
		if(ord(i) + 13 < ord('z')):
			decode += chr(ord(i) + 13)
		else:
			remainder = 12 - (ord('z') - ord(i))
			decode += chr(ord('a') + remainder)
	elif(ord(i) >= ord('A') and ord(i) <= ord('Z')):

		if(ord(i) + 13 < ord('Z')):
			decode += chr(ord(i) + 13)
		else:
			remainder = 12 - (ord('Z') - ord(i))
			decode += chr(ord('A') + remainder)
	else: decode += i

print(decode)

# The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
