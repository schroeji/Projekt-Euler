c = 1001*1001
g = [1]
count = 0
last = 1
ink = 2
for i in range(1,c+1):
    if(i == (last + ink)):
        g.append(i)
       # print(i);
        last = i
        count = count + 1
        if(count == 4):
            ink = ink + 2
            count = 0
print(g)
print(sum(g))