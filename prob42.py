t = []
def is_tria(x):
    value = sum([ord(i) - 64 for i in x])
    if(value in t):
        return True
    elif(t[len(t) - 1] > value):
        return False
    else:
        while(t[len(t) - 1] < value):
            t.append( t[len(t) - 1] + ( t[len(t) - 1] - t[len(t) - 2]) + 1)
        return t[len(t) - 1] == value
t.append(1)
t.append(3)
print(t[len(t) - 1])
f = open('prob42file', 'r')
inp = f.readline()
inp = inp[1: -1]
arr = inp.split('","')

i = 0
for x in arr:
    if(is_tria(x)):
        i = i+1
print(i)