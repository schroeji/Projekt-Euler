def chain_len(x):
	count = 1	
	while(x != 1):
		if(x % 2 == 0):
			x = x/2
		else:
			x = 3*x + 1
		count = count + 1
	return count
longestlen = 1
longestnum = 1
for i in range(1,1000000):
	ilen = chain_len(i)
	if(ilen > longestlen):
		longestlen = ilen
		longestnum = i
print(longestnum)
print(longestlen)
