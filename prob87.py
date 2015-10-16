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


def calc_prime_sum_ways(upperbound):
    global _known_primes
    a = Set()
    _known_primes += [x for x in range(5,int(upperbound**(1.0/2) + 2), 2) if is_prime(x)]
    k_primes = Set(_known_primes)

    quads = [i**2 for i in k_primes.intersection( Set(range(2,int(upperbound**(1.0/2)) + 2)))]
    cubes = [i**3 for i in k_primes.intersection( Set(range(2,int(upperbound**(1.0/3)) + 2))) ]
    fourths = [i**4 for i in k_primes.intersection( Set(range(2,int(upperbound**(1.0/4)) + 2)) )]
    a = Set()
    for quad in quads:
        for cube in cubes:
            for fourth in fourths:
                if(quad + cube + fourth < upperbound):
                    a.add(quad + cube + fourth)
    return len(a)
    
print calc_prime_sum_ways(50000000)

