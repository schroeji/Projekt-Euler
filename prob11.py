readfile = open('prob11file','r')
array = []
for line in readfile:
	array.append(line.split())
i = 0
j = 0
biggestprod = 1
while(i < len(array)):
	while(j < len(array[i])):
		if(j < len(array[i]) - 3):
			tempprod1 = int(array[i][j])
		if(i < len(array) - 3):
			tempprod2 = int(array[i][j])
		if((i < len(array) - 3) and (j < len(array[i]) - 3)):
			tempprod3 = int(array[i][j])
		if((i >= 3) and (j < len(array[i]) - 3)):
			tempprod4 = int(array[i][j])
			for k in range(1,4):
				if(j < len(array[i]) - 3):
					tempprod1 = tempprod1 * int(array[i][j + k])
				if(i < len(array) - 3):
					tempprod2 = tempprod2 * int(array[i + k][j])
				if((i < len(array) - 3) and (j < len(array[i]) - 3)):
					tempprod3 = tempprod3 * int(array[i + k][j + k])
				if((i > 2) and (j < len(array[i]) - 3)):
					tempprod4 = tempprod4 * int(array[i - k][j + k])
			biggestprod = max(tempprod1,tempprod2,tempprod3,tempprod4,biggestprod)
		j = j + 1
	j = 0
	i = i + 1
print(biggestprod)
