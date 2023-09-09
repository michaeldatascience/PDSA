# DFS using recursion
# visited and parent are declared globally
# No explicit Queue maintained due to recursion

(visited, parent) = ({},{})

# they also need tobe initialized
def DFSInitGlobal(AList):
  for i in AList.keys():
    visited[i] = False
    parent[i] = -1  


def DFSGlobal(AList,v):
  visited[v] = True

  for k in AList[v]:
    if(not visited[k]):
      parent[k] = v
      DFSGlobal(AList,k)
 
  return (visited,parent)


#A = {0: [1, 4], 1: [2], 2: [0], 3: [4, 6], 4: [0, 3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
#DFSInitGlobal(A)
#print(DFSGlobal(A,7))



# DFS without recursion. Using stack
# Application. List all paths between two vertices in an undirected graph

def DFS_AllPath(AList, start,end):
  (visited, parents) = ({},{})
  
  for i in range (max(AList.keys())+1):
    visited[i] = False
    parents[i]= -1

  Stack = []
  Paths={}
  currentpath=[]
  pathcount = 0
  # Adding starting to stack
  Stack.append(start)

  while (Stack):
  # Get the next element from stack
  # Check if already not visited
  # mark as visited
  # place it in current path
  #     
    nextNode = Stack.pop()
    if not visited[nextNode]:
      visited[nextNode] = True
      currentpath.append(nextNode)
      if nextNode == end:
        print(currentpath)
        Paths[pathcount] = currentpath.copy()
        pathcount +=1

      for neighbor in AList[nextNode]:
        if not visited[neighbor]:
          Stack.append(neighbor)
    
    #return Paths

A = {0: [1, 4], 1: [2], 2: [0], 3: [4, 6], 4: [0, 3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
start = 0
end = 8
print(DFS_AllPath(A,start,end))
