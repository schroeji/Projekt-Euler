def wert(xstr):
    temp = 0
    for i in xstr:
        temp = temp + (ord(i) - 64)
    return temp
    
f = open('prob22file', 'r')
inp = f.readline()
inp = inp[1: -1]
arr = inp.split('","')
arr.sort()


erg = 0
for x in range(0,len(arr)):
    erg = erg + (x+1)*wert(arr[x])
