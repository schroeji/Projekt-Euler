def is_perm(x,y):
    x = str(x)
    y = str(y)
    if(len(x) != len(y)):
        return False
    for i in x:
        if(i not in y):
            return False
        y.replace(i,'',1)
    return True
    
def is_perm_list(x):
    for i in range(0,len(x) - 1):
        if(not is_perm(x[i],x[i+1])):
            return False
    return True

for x in range(1,10**7):
    if(is_perm_list([x,2*x,3*x,4*x,5*x,6*x])):
        print(x)