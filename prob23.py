from sets import Set
def divList(x):
    retList = [1]
    
    for i in range(2,int(x**0.5) + 1):
        if(x % i == 0):
            retList.append(i)
            if(i != x/i):
                retList.append(x/i)
    return retList

def is_abundant(x):
    
	return sum(divList(x)) > x
 

array = []
for a in range(12,28124):
	if(is_abundant(a)):
		array.append(a)
setOfSumsOfTwoAbundantNumbers = Set()
lol = []
for a in array:
    for b in array:
        if (a + b > 28123):
            break
        setOfSumsOfTwoAbundantNumbers.add(a+b)
abc = range(1,28124)
for i in setOfSumsOfTwoAbundantNumbers:
    abc.remove(i)
print(sum(abc))
