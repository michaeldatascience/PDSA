def allPaths(AList,start,end):
    def DFS(AList,start,end,visited,curr,path):
        visited[start] =True
        curr.append(start)
        if start == end:
            path.append(curr.copy())
        else:
            for neighbor in AList[start]:
                if not visited[neighbor]:
                    DFS(AList,neighbor,end,visited,curr,path)

        
        curr.pop()
        visited[start] = False

    
    Paths = []
    Visited = {i:False for i in range(len(AList))}
    DFS(AList,start,end,Visited,[],Paths)

    return Paths

def countComponents(AList):
    def DFS(AList,start,visited):
        visited[start] = True
        Stack = [start]

        while Stack:
            nextV = Stack.pop()
            for neighbor in AList[nextV]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    Stack.append(neighbor)



    visited = {i: False for i in range(len(AList))}
    Components = 0
    for nextNode in visited:
        if not visited[nextNode]:
            DFS(AList, nextNode, visited)
            Components +=1

    return Components


# Using DFS and maintain a visited dictionary traverse through all unvisited nodes and update the visited list
def _countComponents(AList):
    def DFS(AList,start,visited):
        visited[start]=True
        Stack=[start]

        while (Stack):
            nextV = Stack.pop()
            for neighbor in AList[nextV]:
                if not visited[neighbor] :
                    visited[neighbor] = True
                    Stack.append(neighbor)



    visited = {i: False for i in range(len(AList))}
    Components = 0
    for nextNode in visited:
        if visited[nextNode] == False:
            DFS(AList,nextNode,visited)
            Components +=1
   
    return Components


def __allPaths(AList,start,end):
    def DFS(AList,start,end,visited,curr,path):
        visited[start]= True
        curr.append(start)
        if start == end:
            path.append(curr.copy())
        else:
            for neighbor in AList[start]:
                if not visited[neighbor]:
                    DFS(AList,neighbor,end,visited,curr,path)

        curr.pop()
        visited[start] = False

    
    Paths=[]
    Visited = {i: False for i in range(len(AList))}
    DFS(AList,start,end,Visited,[],Paths)
    
    return Paths

def _allPaths(AList,start,end):

    def DFS(AList, start, end, visited, curr, path):
        # visited is global, initialized to False
        # path is global empty for recursion
        # curr is local empty to support recursion
        visited[start] = True
        curr.append(start)
        if start==end:
            path.append(curr.copy())
        else:
            for neighbor in AList[start]:
                if not visited[neighbor]:
                    DFS(AList,neighbor,end,visited,curr,path)        

        curr.pop()
        visited[start] = False
        
    path = []
    visited = {i: False for i in range(len(AList))}
    DFS(AList, start, end, visited, [], path)

    return path

# Testing on a sample graph
AList = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3, 5],
    5: [4]
}

AList2 = {
    0: [1, 3],
    1: [0, 2, 3, 4],
    2: [1, 4],
    3: [0, 1, 4, 5],
    4: [1, 2, 3, 6],
    5: [3, 6],
    6: [4, 5]
}

start, end = 0, 6
#print(f"Number of connected components: {countConnectedComponents(AList)}")

#print(f"Number of connected components: {countComponents(AList)}")

print(f"All Paths between: {start} and {end}  {allPaths(AList2,start,end )}")