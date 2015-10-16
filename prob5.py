def is_divable(x):
	for i in range(1,21): 	
		if(x % i != 0): 
			return False
	return True
stop = False
i = 10000
while(stop == False):
	if(is_divable(i)):
		stop = True
		print i
	else :
		i = i + 20

