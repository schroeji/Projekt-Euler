import re


def bin_search(lower, upper):
    begin_upper = upper
    while(lower <= upper):
        mid = lower + (upper - lower)/2
        log_s = round(log_sum(mid, begin_upper),15)
        if( log_s == t ):
            return mid
        elif (log_s < t):
            lower = mid + 1
        elif (log_s > t):
            upper = mid - 1
p = re.compile('1\d2\d3\d4\d5\d6\d7\d8\d9\d0')
print 1300000000**2

print len(str(1300000000**2))

for i in range(1000000030, 1400000000, 10):
    l = i ** 2
    if(p.match(str(l)) != None):
        print i 
        break
