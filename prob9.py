for a in range(110,400):
	for b in range(a,400):
		if(a + b + (a**2 + b**2)**0.5 == 1000):
			print(a * b * (a**2 + b**2)**0.5)

