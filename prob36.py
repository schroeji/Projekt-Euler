def is_pali(x):
	s = str(x)
	for i in range(0, len(s)):
		if(s[i] != s[len(s) - 1 - i]):
			return False
	return True

t= []
for i in range(0,1000000):
     if(is_pali(i) and is_pali(bin(i)[2:])):
         t.append(i)
print(sum(t))