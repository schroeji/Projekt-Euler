def is_pali(x) :
	s = str(x)
	for i in range(0, len(s)):
		if(s[i] != s[len(s) - 1 - i]):
			return False
	return True

for a in range(900, 1000):
	for b in range(900,1000):
		if(is_pali(a*b) == True):
			print(a*b)

