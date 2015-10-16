import math
base = 2
t = -(1.0/base)
def log_sum(x, y):
    return math.log(x/float(y), base) + math.log((x - 1)/float(y - 1), base)

def bin_search(upper):
    begin_upper = upper
    lower = 1
    while(lower <= upper):
        mid = lower + (upper - lower)/2
        log_s = round(log_sum(mid, begin_upper),15)
        if( log_s == t ):
            return mid
        elif (log_s < t):
            lower = mid + 1
        elif (log_s > t):
            upper = mid - 1

print bin_search(119)
for i in range(10**12, 10**12 + 1000000):
    l = bin_search(i)
    if l != None:
        print i
        print l
    
