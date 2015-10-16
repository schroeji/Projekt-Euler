
def fill_primes(bound):
    
    for i in range(3, bound + 1, 2):
        noprime = False
        for j in range(3, int(i ** 0.5) + 1, 2):
            if(i % j == 0):
                noprime = True
                break
        if(not noprime):
            primes.append(i)

def is_trunc_prime(x): 
    for i in range(1, len(str(x))):
        l_to_r = int(str(x)[i:len(str(x))])
        r_to_l = int(str(x)[0: -i])
        if(not l_to_r in primes):
            return False
        if(not r_to_l in primes):
            return False
    return True
    

primes = [2]
fill_primes(1000000)

trunc = []

for i in primes :
    if(is_trunc_prime(i)):
        trunc.append(i)
    
print(sum(trunc))