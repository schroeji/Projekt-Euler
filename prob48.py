erg = 0
for i in range(1,1001):
    erg = erg + i**i
print(str(erg)[-10:len(str(erg))])