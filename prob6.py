summe = 0
smallsum = 0
for i in range(0,101):
	summe = summe + i**2
	smallsum = smallsum + i
print(smallsum**2 - summe)
