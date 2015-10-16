def greedy(array):
	returnlist = []
	returnlist.append(array[0][0])
	j = 0	
	i = 0
	while(i < len(array) - 1):
		if(array[i + 1][j] > array[i + 1][j + 1]):
			returnlist.append(array[i + 1][j])
		else:
			returnlist.append(array[i + 1][j + 1])
			j = j + 1
		i = i + 1
	return returnlist

def edgelist(array):
	sumofedges = []
	sumofedges.append([array[0][0]])
	i = 1
	while(i < len(array)):
		suminline = []
		j = 0
		while(j < len(array[i])):
			if(j == 0):
				suminline.append(int(sumofedges[i - 1][j]) + int(array[i][j]))
			elif(j == len(array[i]) - 1):
				suminline.append(int(sumofedges[i - 1][j - 1]) + int(array[i][j]))
			else:
				suminline.append(max(int(sumofedges[i - 1][j - 1]) + 
				int(array[i][j]), int(sumofedges[i - 1][j]) + int(array[i][j])))
			j = j + 1
		sumofedges.append(suminline)
		i = i + 1
	return sumofedges[len(sumofedges) - 1]
	
readfile = open('prob18file','r')
array = []
for line in readfile :
	array.append(line.split())
edgelist = edgelist(array)
print(max(edgelist))
	
