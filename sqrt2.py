"""
Use Binary Search to find a float that differs from sqrt(2) by less than 10**(-6)

"""
import math
def sqrt2():
	l = 1
	r = 2
	while r-l >10**(-6):
		m = (r + l)/2
		if m**2 == 2:
			print("yes!\t", m)
			return m
		elif m**2 < 2:
			l = m
		else:
			r = m
	print("yes!\t", l)
	return l

sqrt2()
print("sqrt(2)=", math.sqrt(2))