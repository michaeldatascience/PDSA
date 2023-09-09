#[ [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4] ]

n = 5   #int(input())
matrix=[]
xval=-1
for i in range(n):
    matrix.append([])
    for j in range(n):
        xval = 1 if i==j else 0
        matrix[i].append(xval)


print(matrix)

