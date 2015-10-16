def is_pan(x):
    x = str(x)
    l = ['1','2','3','4','5','6','7','8','9']
    if len(x) != 9:
        return False
    for c in x:
        try:
            l.remove(c)
        except:
            return False
    return len(l) == 0
    
def last_9(x):
    return x % 10**9
def first_9(x):
    return x / 10**(len(str(x)) - 9)
c1 = 1
fib_n = 1
temp = 1
n = 2
while not ( is_pan(last_9(fib_n)) and is_pan( first_9(fib_n) ) ) :
    temp = fib_n
    fib_n = fib_n + c1
    c1 = temp
    n += 1
    
    
    if(n % 10000 == 0):
        print n
print n