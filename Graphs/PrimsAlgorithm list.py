import numpy as np
def primlist(WList):
    # Calculate infinity based on the maximum edge weight
    infinity = 1 + max(d for u in WList for (_, d) in WList[u])
    
    # Initialize visited and distance dictionaries, and TreeEdges list
    visited = {v: False for v in WList}
    distance = {v: infinity for v in WList}
    TreeEdges = []

    # Start from vertex 0
    visited[0] = True
    for (v, d) in WList[0]:
        distance[v] = d

    # For each vertex, find the shortest edge not in the MST yet
    for _ in WList:
        mindist, nextv, nexte = infinity, None, None
        for u in WList:
            for (v, d) in WList[u]:
                # If vertex u is visited, vertex v is not, and distance is less than mindist
                if visited[u] and not visited[v] and d < mindist:
                    mindist, nextv, nexte = d, v, (u, v)
        
        # Exit loop if no vertex found
        if nextv is None:
            break

        # Mark the next vertex as visited and add the edge to the MST
        visited[nextv] = True
        TreeEdges.append(nexte)

        # Update distances from the next vertex
        for (v, d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v], d)

    return TreeEdges



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

#print(primlist(WMat))


def primlist2(WList):
    # Calculate infinity based on the maximum edge weight
    infinity = 1 + max(d for u in WList for (_, d) in WList[u])
    
    # Initialize visited, distance, and neighbor (nbr) dictionaries
    visited = {v: False for v in WList}
    distance = {v: infinity for v in WList}
    nbr = {v: -1 for v in WList}

    # Start from vertex 0
    visited[0] = True
    for (v, d) in WList[0]:
        distance[v], nbr[v] = d, 0

    # For each vertex, find the closest non-included vertex
    for _ in range(1, len(WList)):
        # Find the vertex with the minimum distance to the MST
        nextd = min(distance[v] for v in WList if not visited[v])
        nextvlist = [v for v in WList if not visited[v] and distance[v] == nextd]
        
        # Exit loop if no vertex found
        if not nextvlist:
            break

        nextv = min(nextvlist)
        visited[nextv] = True

        # Update distances and neighbors for the vertices adjacent to the chosen vertex
        for (v, d) in WList[nextv]:
            if not visited[v] and d < distance[v]:
                distance[v], nbr[v] = d, nextv

    return nbr



A = {0: [(1, 10), (2, 50), (3, 300)], 1: [(0, 10), (2, 30), (6, 65), (3, 40)], 2: [(0, 50), (1, 30), (5, 76), (4, 20)], 3: [(0, 300), (1, 40), (4, 60)], 4: [(6, 37), (3, 60), (2, 
20)], 5: [(6, 45), (2, 76)], 6: [(5, 45), (4, 37), (1, 65)]}

print(primlist2(A))

