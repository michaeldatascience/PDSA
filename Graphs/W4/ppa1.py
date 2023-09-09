# Perform BFS
# Maintain a list Component[vertex]
# 

def findComponents_undirectedGraph(vertices, edges):

    def BFS(start,edges,unvisited):
        print (f'BFS({start},{len(edges)},{len(unvisited)})')
        Q = set()
        Q.append(start)
        #unvisited.remove(start) 
        print (Q)
        while Q:
            node = Q.pop(0)
            Visited.append(node)
            unvisited.remove(node)
            nextNode = -1

            for nextE in edges:
                if (nextE[0])==node:
                    nextNode = (nextE[1])
                elif (nextE[1])==node:
                    nextNode = (nextE[0])
                
                if nextNode != -1:
                    if (nextNode) in unvisited:
                        Q.append((nextNode))

        return Visited

    component = 0
    Visited = []
    Unvisited = set(vertices)
    while Unvisited:
        start_vertex = next(iter (Unvisited))
        print(f'BFS({start_vertex})')
        print(BFS(start_vertex,edges,Unvisited))
        component+=1

    



vertices = ['1', '2', '3', '4', '5', '6', '7', '8'] 
edges =[('1', '3'), ('3', '4'), ('3', '7'), ('5', '6'), ('5', '8'), ('6', '8')]

allcomponents = findComponents_undirectedGraph(vertices, edges)
print(allcomponents)
