from fractions import *
largest_x = 0
for D in range(7,1001):
    y = 1
    if not (D**0.5 == int(D**0.5)):
        while True: 
            x = (1+D*y**2)**0.5
            if x - int(x) == 0:
                largest_x = max(x,largest_x)
                break
            y += 1
            if y > 100000:
                break
print largest_x

"""for D in range(2,8):
    a = Fraction(D)
    x = (a.numerator + 1)**0.5
    y = a.denominator**0.5
    b = Fraction(x).limit_denominator(100).denominator
    x = x * b
    y = y * b
    print str(x) + "/" + str(y)"""