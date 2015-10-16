def gaus_sum(x):
	return x*(x+1)/2
def divcount(x):
	count = 0
	for i in range(1,int(x**0.5) + 1):
		if(x % i == 0):
			count = count + 1
	return 2*count
x = 5
print(divcount(gaus_sum(2)))
print(divcount(gaus_sum(3)))
print(divcount(gaus_sum(4)))
print(divcount(gaus_sum(5)))
print(divcount(gaus_sum(6)))
print(divcount(gaus_sum(7)))
while(divcount(gaus_sum(x)) < 500):
	x = x + 1
print(gaus_sum(x))
