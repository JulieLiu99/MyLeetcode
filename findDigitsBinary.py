def digitsInBinaryRepresentation(num):
	p = 0
	digits = 0

	while num >= pow(2,p):
		digits += 1
		p += 1
		num -= pow(2,p)
	if num > 0: digits += 1
	print(digits)

digitsInBinaryRepresentation(1) # 1
digitsInBinaryRepresentation(4) # 10
digitsInBinaryRepresentation(9) # 101