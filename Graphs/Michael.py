def dijkstraList(AList, s):
    #print (AList)
    # 1. Calculate Infinity
    # 2. Initialize dictionaries distance visited
    # 3. set start vertex as visited
    # 4. Loop
    # 4.1  Calculate Minimum Distance among unvisited Nodes
    # 4.2  Find minimum vertex from the above list as NextVertex
    # 4.2.1  Iterate through all neighbors of this nextVertex
    # 4.2.2  Mark this nextVertex as visited
    # 4.2.3  Recalculate distance of the neighbor

    # 1. Infinity

    infinity = 1 + len(AList.keys()) * max(dist for subitem in AList.values() for _,dist in subitem)
    print(infinity)
    distance,visited = ({},{})
    for i in AList.keys():
        distance[i] = infinity
        visited = 0
    
    distance[s] = 0

    for u in AList.keys():
        nextDist = min([distance[v] for v in AList.keys() if not visited[v]] )
        nextVList = [v for v in AList.keys() if not visited[v] and distance[v] == nextDist] 
        if nextVList == []:
            return
        nextV = min(nextVList)
        for (v,d) in AList[nextV]:
            if not visited[v]:
                distance[v] = min(distance[v] , distance[nextV] + d)

        return (distance)



A = {0: [(1, 10), (2, 50), (3, 300)], 1: [(0, 10), (2, 30), (6, 65), (3, 40)], 2: [(0, 50), (1, 30), (5, 76), (4, 20)], 3: [(0, 300), (1, 40), (4, 60)], 4: [(6, 37), (3, 60), (2, 
20)], 5: [(6, 45), (2, 76)], 6: [(5, 45), (4, 37), (1, 65)]}

result  = dijkstraList(A, 3)
print(result)