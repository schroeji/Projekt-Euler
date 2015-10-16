def is_ami(x,y):
	xsum = 0
	ysum = 0
	for i in range(1,int(x**0.5) + 1):
		if(x % i == 0):
			xsum = xsum + i
			if(i != x**0.5 and i != 1):
				xsum = xsum + x/i
	for i in range(1,int(y**0.5) + 1):
		if(y % i == 0):
			ysum = ysum + i
			if(i != y**0.5 and i != 1):
				ysum = ysum + y/i
	return (ysum == x) and (xsum == y)
	
def divList(x):
    retList = [1]
    
    for i in range(2,int(x**0.5) + 1):
        if(x % i == 0):
            retList.append(i)
            retList.append(x/i)
    return retList
 
erg = 0
skip = []
for i in range(1,10000):
    if (not i in skip):
        j = sum(divList(i))
        if(is_ami(i,j) and i != j):
            erg = erg + i + j
            skip.append(j)
print(erg)
