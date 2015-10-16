from sets import Set

def find_prime_factorials(x):
    ret_primes = Set()
    while (not x in primes):
        for i in primes:
            if (x % i == 0):
                ret_primes.add(i)
                x = x /i
                break
    ret_primes.add(x)
    return ret_primes
    
def get_divs(x):
    ret = Set()
    for i in range(2,int(x**0.5) + 1):
        
        if(x % i == 0):
            ret.add(i)
            ret.add(x/i)
            
    return ret

primes = [2]

def fill_primes(lowerbound,upperbound):
    
    for i in range(lowerbound, upperbound + 1, 2):
        noprime = False
        for j in range(3, int(i ** 0.5) + 1, 2):
            if(i % j == 0):
                noprime = True
                break
        if(not noprime):
            primes.append(i)


def is_perm(x,y):
    x = str(x)
    y = str(y)
    if(len(x) != len(y)):
        return False
    for i in x:
        if(i not in y):
            return False
        y.replace(i,'',1)
    return True

def phi(n):
    ret = n
    for i in find_prime_factorials(n):
        ret = ret*(1-(1.0/i))
    return ret
    """
fill_primes(3,100000)
for i in range(2,100):
    print(str(i) + ":" + str(phi(i)))
    print(find_prime_factorials(i))
"""
min1 = 2.0
fill_primes(3,10**7)
for i in range(3,10**7,2):
    p = phi(i)
    if(i % 10001 == 0):
        print(i)
    if(min1 > i/p and is_perm(i,p)):
        min1 = i/p
        min_i = i
print(min_i)