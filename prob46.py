def fill_primes(bound):
    
    for i in range(3, bound + 1, 2):
        noprime = False
        for j in range(3, int(i ** 0.5) + 1, 2):
            if(i % j == 0):
                noprime = True
                break
        if(not noprime):
            primes.append(i)
    

def sum_of_prime_square(x):
    if(x in primes):
        return True
    for i in primes:
        if(i >= x):
            break
        a = x - i
        a = a / 2
        if(a**0.5 - int(a**0.5) == 0):
           return True
    return False

primes = [2]
fill_primes(100000)

i = 9
while(True):
    if(not sum_of_prime_square(i)):
        print(i)
        break
    i = i + 2