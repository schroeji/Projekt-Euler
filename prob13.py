read = open('prob13file', 'r')
erg = 0
for line in read:
	erg = erg + int(line)
	
print(erg)

