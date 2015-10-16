def valid_tria(x,y,z):
    return x**2 + y**2 == z**2

def sing_tria(ges_len):
    c = 0
    for x in range (1,ges_len/3 + 1):
        for y in range(x,(2*ges_len)/3 + 2):
            z = ges_len -(x+y)
            if valid_tria(x,y,z):
                c += 1
                if c > 1:
                    return False
    return True
    
c = 0
for i in range(12,1500000):
    c = c + 1 if sing_tria(i) else c
print c
