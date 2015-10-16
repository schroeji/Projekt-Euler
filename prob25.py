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
x = 50
a = len(str(fib(x)))
while(a < 1000):
	x = x + 1;
	a = len(str(fib(x)))
	print(a)
print(x)

