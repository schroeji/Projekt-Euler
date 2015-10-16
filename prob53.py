t = {}

def fill_binos(bound):
    for n in range(1,bound):
        t[(n,0)] = 1
        t[(n,n)] = 1
    for n in range(2,bound):
        for k in range(1,n):
            t[(n,k)] = t[(n-1,k-1)] + t[(n - 1,k)]
            
fill_binos(101)
c = 0
for i in t:
    if (t[i] > 1000000):
        c = c + 1
print (c)
        