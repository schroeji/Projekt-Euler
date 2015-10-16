max_count = 0
ind = 0
for i in range(7,1000):
    remainders = []
    a = 10 % i
    count = 0
    while(not a in remainders):
         remainders.append(a)
         a = (remainders[len(remainders) - 1] * 10) % i
         count = count + 1
         if(max_count < count):
             max_count = count
             ind = i
print(ind)
print(max_count)