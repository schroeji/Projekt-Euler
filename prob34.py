faks = {0 : 1, 1 : 1}
 
def is_fac_sum(x) :
    a = 0
    for i in str(x):
        a = a + faks[int(i)]
    return a == x
 
for i in range(2,10):
    faks[i] = faks[i-1] * i
t = []
print(is_fac_sum(1))
for i in range(3, 1000000):
    if(i % 500000 == 0):
        print(i)
    if(is_fac_sum(i)):
        t.append(i)
print(sum(t))   