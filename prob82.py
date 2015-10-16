from Queue import Queue, PriorityQueue
f = open("prob82file",'r')
matrix = []
for line in f:
    matrix.append( map(int, line.split(",")) )


queue = PriorityQueue()
for i in range(0,80):
    queue.put( (matrix[i][0], (i,0) ) )
    dic = {(i,0) : matrix[i][0]}
while (not queue.empty() ):
    summe, (i,j) = queue.get()
    if (i,j) == (i,79):
        print summe
        break
    if(i < len(matrix) - 1):
        try:
            if(dic[(i+1,j)] > summe + matrix[i+1][j]):
                queue.put( (summe + matrix[i+1][j], (i+1,j)) )
                dic[(i+1,j)] = summe + matrix[i+1][j]
        except:
           queue.put( (summe + matrix[i+1][j], (i+1,j)) )
           dic[(i+1,j)] = summe + matrix[i+1][j]
           
    if(j < len(matrix) - 1):
        try:
            if(dic[(i,j + 1)] > summe + matrix[i][j + 1]):
                queue.put( (summe + matrix[i][j + 1], (i,j+ 1)) )
                dic[(i,j+ 1)] = summe + matrix[i][j+ 1]
        except:
            queue.put( (summe + matrix[i][j+ 1], (i,j+ 1)) )
            dic[(i,j+ 1)] = summe + matrix[i][j+ 1]
    
    if(i > 0):
        try:
            if(dic[(i-1,j)] > summe + matrix[i-1][j]):
                queue.put( (summe + matrix[i-1][j], (i-1,j)) )
                dic[(i-1,j)] = summe + matrix[i-1][j]
        except:
           queue.put( (summe + matrix[i-1][j], (i-1,j)) )
           dic[(i-1,j)] = summe + matrix[i-1][j]

    

            