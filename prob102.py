from numpy import linalg

def trivial_reject(a,b,c,p):
    
    if ( (a[0] > p[0]) and (b[0] > p[0]) and (c[0] > p[0]) ) or ( (a[0] < p[0]) and (b[0] < p[0]) and (c[0] < p[0]) ):
        return True
    if ( (a[1] > p[1]) and (b[1] > p[1]) and (c[1] > p[1]) ) or ( (a[1] < p[1]) and (b[1] < p[1]) and (c[1] < p[1]) ):
        return True
    return False
def is_point_in_tria(a,b,c,p):
    if trivial_reject(a,b,c,p):
        return False
    [a,b,c] = sorted([a,b,c])
    #print [a,b,c]
    ab =  (b[0] - a[0],b[1] - a[1])
    ac = (c[0] - a[0],c[1] - a[1])
    pa = (p[0] - a[0],p[1] - a[1])
    matrix_a = [ [ab[0],ac[0]] , [ ab[1],ac[1] ] ]
    sol = linalg.solve(matrix_a, pa)
    #print sol
    """if False == (not trivial_reject(a,b,c,p)) == (not ( (0 <= sum(sol) <= 1) and (0 <= sol[0] <= 1) and (0 <= sol[1] <= 1) ) ):
        print trivial_reject(a,b,c,p)
        print ( (0 <= sum(sol) <= 1) and (0 <= sol[0] <= 1) and (0 <= sol[1] <= 1) )
        print [a,b,c]
        print sol"""
    return (0 <= sum(sol) <= 1) and (0 <= sol[0] <= 1) and (0 <= sol[1] <= 1) 
def read_trias(f):
    trias = []
    for line in f:
        coords = line.strip().split(",")
        coords = map(int,coords)
        trias.append( ((coords[0],coords[1]),(coords[2],coords[3]),(coords[4],coords[5]))  )
    return trias
point = (0,0)

f = open("prob102file",'r')
trias = read_trias(f)
a,b,c = trias[0]
#print is_point_in_tria(a,b,c,point)
a,b,c = trias[1]
#print is_point_in_tria(a,b,c,point)
print sum([1 for a,b,c in trias if is_point_in_tria(a,b,c,point) ])
    