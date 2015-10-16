def digit_square_sum(x):
    x = str(x)
    return sum([int(i)**2 for i in x])

def chain_89(x):
    while( x != 89 and x != 1):
        x = digit_square_sum(x)
    return x == 89

c = 0
for i in range(1,10000000):
     c = c + 1 if chain_89(i) else c
     
print c