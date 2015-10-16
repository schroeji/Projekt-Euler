def is_pali(x):
	s = str(x)
	for i in range(0, len(s)):
		if(s[i] != s[len(s) - 1 - i]):
			return False
	return True

def rev_add(x):
    return x + int(str(x)[::-1])
    
def is_lychrel(x):
    for i in range(1,51):
        x = rev_add(x)
        if( is_pali(x)):
            return False
    return True
c = 0
for i in range(1,10001):
    if(is_lychrel(i)):
         c += 1
print(c)