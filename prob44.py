def p(n):
    return n*(3*n-1)/2
inv_p = {}
 
for i in range(1,1000000):
   inv_p[p(i)] = i
 
D = 9999999999999
print(p(1000))
for i in range(1,10000):
    for j in range(i + 1,10001):
        try:
            inv_p[p(j) - p(i)]
            print("pass1")
            inv_p[p(j) + p(i)]
            print("pass2")
            if(p(j) - p(i) < D):
                print("kleiner")
                D = p(j) - p(i)
        except:
            pass
    print(i)
print(D)