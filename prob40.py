a = "0"
for i in range(1,500000):
    a = a + str(i)
erg = int(a[10]) * int(a[100])* int(a[1000]) * int(a[10000])* int(a[100000]) * int(a[1000000])
print(erg)