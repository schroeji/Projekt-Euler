from sets import Set
s = Set()
for i in range(2,101):
    for j in range(2,101):
        s.add(i**j)
print(len(s))
#print(s)