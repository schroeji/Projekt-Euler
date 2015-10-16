from sets import Set

def prod_exists(x):
    x = str(x)    
    for i in range(1,5):
        for j in range(1, 8 - i):
            if (int(x[:i]) * int(x[i:i + j]) == int(x[i+j:])):
                return int(x[i+j:])
    return 0

facs = {}
def fac(x):
    try: return facs[x]
    except:
        if(x == 1 or x == 0):
            facs[x] = 1
            return 1
        facs[x] = x*fac(x-1)
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
    
perms = gen_perms(123456789)

print(sum( Set(prod_exists(i) for i in perms) ))