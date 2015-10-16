def dig_cancel(x,y):
    if(int(x) % 10 == 0 or int(y) % 10 == 0): #trivialer Fall
        return False
    x = str(x)
    y = str(y)
    
    if(x[0] == y[0]):
        if( float(x[1])/float(y[1]) == float(x) / float(y) ):
            return True
            
    if(x[0] == y[1]):
        if( float(x[1])/float(y[0]) == float(x) / float(y) ):
            return True
    
    if(x[1] == y[0]):
        if( float(x[0])/float(y[1]) == float(x) / float(y) ):
            return True
    
    if(x[1] == y[1]):
        if( float(x[0])/float(y[0]) == float(x) / float(y) ):
            return True
    
    return False

t = []
for denom in range(11,100):
    for nom in range(10, denom):
        if dig_cancel(nom,denom):
            t.append((nom,denom))
ergnom = 1.0
ergdenom = 1.0
for (nom,denom) in t:
    ergnom *= nom
    ergdenom *= denom
print (ergdenom/ergnom)