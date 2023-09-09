import numpy as np
def floydwarshall(WMat):
    # Get matrix dimensions
    rows, cols, x = WMat.shape
    
    # Calculate infinity based on max weight in matrix and number of rows
    infinity = np.max(WMat[:,:,1]) * rows * rows + 1

    # Initialize shortest paths matrix with infinity values
    SP = np.full((rows, cols, cols+1), infinity)
    
    # Assign edge weights to the SP matrix from WMat
    for i in range(rows):
        for j in range(cols):
            if WMat[i, j, 0] == 1:  # If there's an edge
                SP[i, j, 0] = WMat[i, j, 1]
    
    # Main loop: For each intermediate vertex, update shortest paths
    for k in range(1, cols+1):
        for i in range(rows):
            for j in range(cols):
                SP[i, j, k] = min(SP[i, j, k-1], SP[i, k-1, k-1] + SP[k-1, j, k-1])

    # Return the shortest paths after considering all intermediate vertices
    return SP[:, :, cols]


WMat = np.zeros((4, 4, 2))  # Initializing a 4x4x2 matrix with zeros

WMat[0, 1, 0] = 1  # Edge from 0 to 1 exists
WMat[0, 1, 1] = 1  # Weight of edge from 0 to 1
WMat[0, 2, 0] = 1  # Edge from 0 to 2 exists
WMat[0, 2, 1] = 4  # Weight of edge from 0 to 2
WMat[1, 2, 0] = 1  # Edge from 1 to 2 exists
WMat[1, 2, 1] = 2  # Weight of edge from 1 to 2
WMat[1, 3, 0] = 1  # Edge from 1 to 3 exists
WMat[1, 3, 1] = 5  # Weight of edge from 1 to 3
WMat[2, 3, 0] = 1  # Edge from 2 to 3 exists
WMat[2, 3, 1] = 1  # Weight of edge from 2 to 3
print(floydwarshall(WMat))



def floydwarshallList(WList):
    # Number of vertices
    vertices = len(WList)
    
    # Calculate infinity based on the maximum edge weight and number of vertices
    infinity = 1 + vertices * max(d for u in WList for (v, d) in WList[u])
    
    # Initialize shortest paths matrix with infinity values
    SP = [[infinity for _ in range(vertices)] for _ in range(vertices)]
    
    # Assign 0 for diagonal (distance to self)
    for i in range(vertices):
        SP[i][i] = 0

    # Assign edge weights to the SP matrix from WList
    for u in WList:
        for (v, w) in WList[u]:
            SP[u][v] = w
    
    # Main loop: For each intermediate vertex k, update shortest paths
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                SP[i][j] = min(SP[i][j], SP[i][k] + SP[k][j])

    # Return the shortest paths matrix
    return SP



AList = {0: [(1, 10), (2, 50), (3, 300)], 1: [(0, 10), (2, 30), (6, 65), (3, 40)], 2: [(0, 50), (1, 30), (5, 76), (4, 20)], 3: [(0, 300), (1, 40), (4, 60)], 4: [(6, 37), (3, 60), (2, 
20)], 5: [(6, 45), (2, 76)], 6: [(5, 45), (4, 37), (1, 65)]}

print(floydwarshallList(AList))
