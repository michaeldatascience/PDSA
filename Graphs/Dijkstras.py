# Matrix Implementation

import numpy as np
def dijkstraWMat(WMat, s): 
    print(WMat)
    print(f'starting from {s}')
    rows, cols, x = WMat.shape
    infinity = np.max(WMat[:,:,1]) * rows + 1
    print(f'infinity: {infinity}')
    visited, distance = {}, {}
    for v in range(rows):
        visited[v], distance[v] = False, infinity
    distance[s] = 0

    # Main loop

    for u in range(rows):
        print(f'Running from node: {u}')
        nextd = min([distance[v] for v in range(rows) if not visited[v]])
        print(f'Next minimum distance from current {u} is {nextd}')
        nextvlist = [v for v in range(rows) if not visited[v] and distance[v] == nextd]
        print(f'Starting from {u} with minimum distance of {nextd} there are {len(nextvlist)} nodes')
        if not nextvlist:
            break
        nextv = nextvlist[0]
        print(f'Next vertex selected {nextv}')
        visited[nextv] = True
        # Update distances using adjacency matrix
        print(f'Checking if any vertex start from {nextv} needs to be updated')
        for v in range(cols):
            if WMat[nextv, v, 0] == 1 and not visited[v]:
                print(f'Updating distance of {v}')
                print(f'print current distance {distance[v]} alternate via {nextv}-{v}: {WMat[nextv, v, 1]}')
                distance[v] = min(distance[v], distance[nextv] + WMat[nextv, v, 1])
                

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

#print(dijkstraWMat(WMat,2))



def dijkstraList(WList, s):
    print(WList)
    infinity = 1 + len(WList) * max(d for _, d in [item for sublist in WList.values() for item in sublist])
    #infinity2 = len(WList) * max(dist for _,dist in  [item for sublist in WList.values() for item in sublist]  )

       
    # Initialize visited and distance dictionaries
    visited = {v: False for v in WList}
    distance = {v: infinity for v in WList}
    distance[s] = 0

    while True:
        # Get unvisited vertex with the shortest distance
        unvisited_distances = {v: d for v, d in distance.items() if not visited[v]}
        if not unvisited_distances:
            break
        nextv = min(unvisited_distances, key=unvisited_distances.get)

        # Mark as visited and update neighbor distances
        visited[nextv] = True
        for (v, d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v], distance[nextv] + d)

        return distance

A = {0: [(1, 10), (2, 50), (3, 300)], 1: [(0, 10), (2, 30), (6, 65), (3, 40)], 2: [(0, 50), (1, 30), (5, 76), (4, 20)], 3: [(0, 300), (1, 40), (4, 60)], 4: [(6, 37), (3, 60), (2, 
20)], 5: [(6, 45), (2, 76)], 6: [(5, 45), (4, 37), (1, 65)]}

print(dijkstraList(A, 3))
