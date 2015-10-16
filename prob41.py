from sets import Set
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 500000, 2) if is_prime(x)]

def perm_gen(domain,nr):
    ret = ""
    l = len(domain)
    for i in range(0,l):
        t = int(nr) / fac(l - i - 1)
        nr = int(nr) % fac(l - i - 1)
        
        ret += str(domain[t])
        domain.remove(domain[t])
    
    return ret

def gen_perms(domain):
    domainlist = []
    domainlist.extend(str(domain))
    domainlist.sort()
    perms = []
    print domainlist
    for i in range(0, fac(len(domainlist))):
        calldomain = domainlist[:]
        perms.append(int(perm_gen(calldomain,i))) 
    return perms

def fac(x):
    
    if(x == 1 or x == 0):
        return 1
    return x*fac(x-1)
    
x = gen_perms(1234567)
x.reverse()
for i in x:
    if is_prime(i):
        print i
