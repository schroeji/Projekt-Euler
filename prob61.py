from sets import Set
import Random
def tria(n):
    return (n*(n+1))/2
def square(n):
    return n*n
def penta(n):
    return (n*(3*n-1))/2
def hexa(n):
    return (n*(2*n-1))
def hepta(n):
    return (n*(5*n-3))/2
def octa(n):
    return n*(3*n - 2)
    
def four_dig_polygonal(polygonal_function):
    i = 1
    ret = []
    poly= polygonal_function(i)
    while len(str(poly)) <= 4 :
        if len(str(poly)) == 4:
            ret.append(poly)
        i += 1
        poly = polygonal_function(i)
    return ret
    
octs = four_dig_polygonal(octa)
hepts = four_dig_polygonal(hepta)
hexs = four_dig_polygonal(hexa)
pentas = four_dig_polygonal(penta)
squares = four_dig_polygonal(square)
trias = four_dig_polygonal(tria)

open_polys = [hepts,hexs,pentas,squares,trias]

for octa in octs:
    last = str(octa)
    Random.
    