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

def is_conc_prod(x):
    x = str(x)
    for i in range(1, len(x)/2 + 1):
        string = ""
        j = 1
        while len(string) < len(x):
            string += str(int(x[:i]) * j)
            j += 1
        if(x == string):
            return True
    return False
#is_conc_prod(192384576)
pans = gen_perms(123456789)
pans.reverse()

for i in pans:
    if is_conc_prod(i):
        print i
        break
