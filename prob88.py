import Set
def get_divs(x):
    ret = Set()
    for i in range(2,int(x**0.5) + 1):
        
        if(x % i == 0):
            ret.add((i,x/i))
            
    return ret
