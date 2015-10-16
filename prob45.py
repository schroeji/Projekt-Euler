from sets import Set
def t(x):
    return int(x*(x+1)*0.5)
def p(x):
    return int(x*(3*x-1)*0.5)
def h(x):
    return x*(2*x-1)
    
ts = Set()
ps = Set()
hs = Set()


for i in range(143,1000000):
    ts.add(t(i))
    ps.add(p(i))
    hs.add(h(i))

temp = ts.intersection(ps.intersection(hs))
print(temp)