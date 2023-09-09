# Matrix Sample
#[ [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4], 
#  [0, 1, 2, 3, 4] ]

# Functions
def ScalarMatrix(rows,scalar):
    matrix=[]
    for i in range(rows):
        matrix.append([])
        for j in range(rows):
            if i==j:
                matrix[i].append(scalar)
            else:
                matrix[i].append(0)
    return matrix 

def ScalarMatrix2(rows,s):
    matrix=[]
    # inner block [ x for x in range(rows) ] is producing a column
    # this becomes expression of the outer block. i.e. [INNERBLOCK] for y in range(rows)
    matrix = [[ x for x in range(rows) ] for y in range(rows)]
    return matrix


def identity_matrix(n):
    matrix=[]
    xval=-1
    for i in range(n):
        matrix.append([])
        for j in range(n):
            xval = 1 if i==j else 0
            matrix[i].append(xval)
    
    #print(matrix)
    return matrix

def identity_matrix2(n):
    matrix = [ [1 if i==j else 0 for i in range(n)] for j in range(n) ]
    return matrix


def prettyprint(Matrix):
    rows = len(Matrix)
    cols = len(Matrix[0])
    for i in range (rows):
        print(Matrix[i])
    
    #print('énd matrix')


# Main Execution
#imatrix = identity_matrix(5)
#smatrix = ScalarMatrix(5,10)
#print(imatrix)
#prettyprint(imatrix)
#prettyprint(smatrix)

#scalar2 = ScalarMatrix2(5,2)
#prettyprint(scalar2)

#identity2 = identity_matrix2(7)
#prettyprint(identity2)


def list_to_string(L):
    strvalue=''
    for i in range(len(L)):
        print(*L[i], sep=',')
        
        
    
def identity_matrix(n):
    matrix=[]
    matrix= [ [1 if x==y else 0 for x in range(n)] for y in range(n)]
    return matrix
    

n = 5 #int(input())
idm = identity_matrix(n)
list_to_string(idm)


'''
(1) Write a function named get_column that accepts a matrix named mat and a non-negative integer named col as arguments. It should return the column that is at index col in the matrix mat as a list. Zero-based indexing is used here.
(2) Write a function named get_row that accepts a matrix named mat and a non-negative integer named row as arguments. It should return the row that is at index row in the matrix mat as a list. Zero-based indexing is used here.
Extract Rows / Columns from matrix
Key idea: repeat for size and keep either row or column fixed
'''
def get_column(mat, col):
    L=[]
    for r in range(len(mat)):
    #for c in range(len(mat[r])):
        L.append(mat[r][col])
    
    return L

def get_row(mat, row):
    L=[]
    #for r in range(len(mat)):
    for c in range(len(mat[0])):
        L.append(mat[row][c])
    
    return L


C=get_column([[1, 2], [3, 4]], 0)
R=get_row([[1, 2], [3, 4]], 1)

print(C)
print(R)
