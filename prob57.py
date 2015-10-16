import fractions
import decimal
def sqrt_expansion(iterations):
    s = decimal.Decimal(2.0)
    decimal.getcontext().prec = 1000
    for i in range(0,iterations):
        if i < iterations - 1:
            s = 2 + decimal.Decimal(1.0)/s
        else:
            s = 1 + decimal.Decimal(1.0)/s
    return s

count = 0
for i in range(1,1001):
     dec = sqrt_expansion(i)
     #print dec
     a = fractions.Fraction(dec).limit_denominator(2**(2*i))
     #print a
     n = str(a.numerator)
     d = str(a.denominator)
     if(len(n) > len(d)):
         count += 1
print count