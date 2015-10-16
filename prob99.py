import math
def pre_filter(plist):
    for (x,y) in plist:
        for (i,j) in plist:
            if((x >= i and y >= j) and (x > i or y > j)):
                plist.remove((i,j))

def calc_log((x,y)):
    return y*math.log10(x)
pairs = []
f = open('prob99file', 'r')
for inp in f:
    pairs.append((int(inp.split(',')[0]),int(inp.split(',')[1])))
pre_filter(pairs)
curr_max = 0

for i in pairs:
    if (calc_log(i) > curr_max):
        curr_max = calc_log(i)
        (x,y) = i
print (x,y)

