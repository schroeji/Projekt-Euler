def is_prime(x):
	for i in range(3, int(x**0.5) + 1, 2):
		if(x % i == 0):
			return False
	return True

stop = False
erg = 0
n = 3
while(stop != True):
		if(is_prime(n)):
			erg = erg + n
		if(n % 10000 == 3):
			print(n)		
		if(n >= 2000000):
			stop = True		
		n = n + 2
print(erg + 2)
