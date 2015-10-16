c = 0
for i in range(1,250):
    for j in range(1,50):
        a = i**j
        if(len(str(a)) == j):
            c += 1
print c