def prop_divs(x):
    max_range = int(x**0.5)
    props = [1]
    if x**0.5 == max_range: #qudarat Zahl
        props.append(max_range)
    else:
        max_range += 1
    for i in range(2,max_range):
        if x % i == 0:
            props.append(i)
            props.append(x/i)
    return props
    
def calc_ami(x):
    s = sum(prop_divs(x))
    chain = [x]

    while s not in chain:
        if(s > 1000000 or s == 1):
            return None
        chain.append(s)
        s = sum(prop_divs(s))
    
    return chain[chain.index(s):]
max_i = 1
max_len = 1
for i in range(100,1000001):
    a = calc_ami(i)
    if a != None:
        if len(a) > max_len:
            max_len = len(a)
            max_i = i
#print calc_ami(203034)
print min(calc_ami(max_i))