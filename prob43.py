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
        #modifikation fuer prob 43
        a = str(perm_gen(calldomain,i))
        if(sub_string_div(a)):
            perms.append(int(a)) 
    return perms

def sub_string_div(x):
    if(int(x[1:4]) % 2 != 0):
        return False
    if(int(x[2:5]) % 3 != 0):
        return False
    if(int(x[3:6]) % 5 != 0):
        return False
    if(int(x[4:7]) % 7 != 0):
        return False
    if(int(x[5:8]) % 11 != 0):
        return False
    if(int(x[6:9]) % 13 != 0):
        return False
    if(int(x[7:10]) % 17 != 0):
        return False
    return True

print sum(gen_perms("0123456789"))

#perms = gen_perms("0123456789")
