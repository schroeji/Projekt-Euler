def fak(x):
    
    if(x == 1 or x == 0):
        return 1
    return x*fak(x-1)
def permNumber(x): #bestimmt die wie vielte Permutation vorliegt
    perm = ['0','1','2','3','4','5','6','7','8','9']
    l = len(x)
    erg = 0
    for i in range(0,l):
        try:
            erg = erg + perm.index(x[i]) * fak(l-i-1)
            perm.remove(x[i])
        except:
            pass
    return erg + 1
number = 1000000
erg = []
"""perm = [0,1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    print("number="+str(number))
    print(fak(10-i))
    temp = number/fak(10-i)
    origtemp = temp
    while(temp in erg):
        temp = temp - 1
    print("origtemp="+str(origtemp))
    erg.append(temp)
    number = number - (origtemp*fak(10-i))
print(erg)"""
print(permNumber("2783915460"))