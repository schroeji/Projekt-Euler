def is_sum_of_fith_powers(x):
    return x == sum([int(i)**5 for i in str(x)]) 
    
g = []
for i in range(2,5000000):
    if(is_sum_of_fith_powers(i)):    
        g.append(i)

print(g)
print(sum(g))