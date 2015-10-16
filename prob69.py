from sets import Set
from fractions import *
import math
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
_known_primes += [x for x in range(5, 10000, 2) if is_prime(x)]


def find_prime_factorials(x): #modifiziert von prob47
    if(is_prime(x)):
        return Set([x])
    else:
        for prime in _known_primes:
            if(x % prime == 0):
               return Set([prime]).union( Set(find_prime_factorials(x/prime)) )

def prod(x):
	ret = 1
	for i in x:
		ret *= i
	return ret

def phi(x):
    return x*prod([1.0 - (1.0/i) for i in find_prime_factorials(x)])

def n_by_phi(n):
	if(n % 1000 == 0):
		print(n)
	return float(n)/phi(n)

phi_dict = {}


"""
for i in range(1,1000001):
    if not i in phi_dict:
        phi_i = int(phi(i))
        print phi_i
        phi_dict.update({i : phi_i})
        for j in range(2, i):
            if(gcd(i,j) == 1 and i*j not in phi_dict):

                phi_dict[i * j] = int(phi_i * phi_dict[j]) """

def find_candidate(bound):
    ret = []
    i = 0
    while(prod(ret)*_known_primes[i] < bound):
        ret.append(_known_primes[i])
        i += 1
    return ret
print( prod(find_candidate(1000000)) )