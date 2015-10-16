def valid_tria(x,y,z):
    return x**2 + y**2 == z**2
    
sols = {}
print(valid_tria(20,48,52))
print(valid_tria(24,45,51))
print(valid_tria(30,40,50))

for p in range(1,1001):
    sols[p] = 0
    print(p)
    for x in range (1,p/3 + 1):
        for y in range(x,(2*p)/3 + 2):
            z = p -(x+y)
            if((x+y+z == p) and valid_tria(x,y,z)):
                sols[p] = sols[p] + 1
print(max(sols.values()))
print(sols[120])
for key in sols:
    if(sols[key] == max(sols.values())):
        print(key)
