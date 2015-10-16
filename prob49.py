from sets import Set
def fill_primes(lowerbound,upperbound):
    
    for i in range(lowerbound, upperbound + 1, 2):
        noprime = False
        for j in range(3, int(i ** 0.5) + 1, 2):
            if(i % j == 0):
                noprime = True
                break
        if(not noprime):
            primes.append(i)
            
def fac(x):
    
    if(x == 1 or x == 0):
        return 1
    return x*fac(x-1)

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
    for i in range(0, fac(len(domainlist))):
        calldomain = domainlist[:]
        perms.append(int(perm_gen(calldomain,i))) 
    return perms

def arith_checker(x):
    x = list(x)
    x.sort()
    for i in range(0,len(x)):
        for j in range(i + 1, len(x) ):
            if ( x[j] + (x[j] - x[i]) in x):
                return [x[i], x[j], x[j] + (x[j] - x[i])]
    return None
primes = []
fill_primes(1001,10000)


primes_set = Set(primes)

print arith_checker(primes_set & Set(gen_perms(1987)))

for i in primes:
    in_set = primes_set & Set(gen_perms(i))
    if( len(in_set)  >= 3):
        if( arith_checker(in_set) != None):
            print arith_checker(in_set)

#print primes
