import numpy as np
def bellmanfordWMat(WMat, s):
    # Get matrix dimensions
    rows, cols, x = WMat.shape

    # Calculate infinity: Max matrix value * number of rows + 1
    infinity = np.max(WMat[:,:,1]) * rows + 1

    # Initialize distance dictionary
    distance = {v: infinity for v in range(rows)}
    distance[s] = 0

    # Main loop: Iterate |V|-1 times (|V| is number of vertices)
    for _ in range(rows - 1):  
        for u in range(rows):
            for v in range(cols):
                # If edge exists between u and v
                if WMat[u, v, 0] == 1:
                    distance[v] = min(distance[v], distance[u] + WMat[u, v, 1])

    # Optional: Check for negative-weight cycles (not included in the given code)
    # for u in range(rows):
    #    for v in range(cols):
    #        if WMat[u, v, 0] == 1 and distance[u] + WMat[u, v, 1] < distance[v]:
    #            print("Graph contains a negative-weight cycle.")
    #            return

    return distance


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
#print(bellmanfordWMat(WMat,2))






def bellmanfordList(WList, s):
    # Calculate infinity based on the maximum weight and number of vertices
    infinity = 1 + len(WList) * max(d for u in WList for (v, d) in WList[u])
    
    # Initialize distances to infinity for all vertices
    distance = {v: infinity for v in WList}
    
    # Set the source vertex distance to 0
    distance[s] = 0

    # Main loop: Iterate |V|-1 times (where |V| is the number of vertices)
    for _ in WList:
        # Update shortest path for all edges
        for u in WList:
            for (v, d) in WList[u]:
                distance[v] = min(distance[v], distance[u] + d)

    return distance

AList = {0: [(1, 10), (2, 50), (3, 300)], 1: [(0, 10), (2, 30), (6, 65), (3, 40)], 2: [(0, 50), (1, 30), (5, 76), (4, 20)], 3: [(0, 300), (1, 40), (4, 60)], 4: [(6, 37), (3, 60), (2, 
20)], 5: [(6, 45), (2, 76)], 6: [(5, 45), (4, 37), (1, 65)]}

print(bellmanfordList(AList,3))