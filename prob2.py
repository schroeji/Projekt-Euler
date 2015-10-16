def fib(x) :
	if((x == 0) or (x == 1)) :
		return x
	else : 
		a = 0
		b = 1
	for i in range(2,x + 1):
		newa = b
		newb = a + b
		a = newa
		b = newb
	return b
erg = 0
for i in range(0,100):
	a = fib(i);
	if ((a % 2 == 0) and a <= 4000000):
		erg = erg + a 
#print fib(100)
print(erg)
