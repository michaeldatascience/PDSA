'''
Standard Algos for BFS, DFS, Topological Sort
'''

def BFS(AList, v):
  visited = {}
  for i in range(max(AList.keys())+1):
    visited[i] = False

  q = []

  visited[v] = True
  q.append(v)

  while q:
    j = q.pop(0)
    for k in AList[j]:
      if(not visited[k]):
        visited[k] = True
        q.append(k)
  return(visited)


def BFS_Path(AList, v):
  (visited, parent) = ({},{})
  for i in range(max(AList.keys())+1):
    visited[i] = False
    parent[i] = -1
  q = []
  visited[v] = True
  q.append(v)

  while q:
    j = q.pop(0)
    for k in AList[j]:
      if(not visited[k]):
        visited[k] = True
        parent[k] =j
        q.append(k)
  return(visited,parent)

def BFS_PathLevels(AList, v):
  (visited, parent, levels) = ({},{},{})
  for i in range(max(AList.keys())+1):
    visited[i] = False
    parent[i] = -1
    levels[i] = -1
  q = []
  visited[v] = True
  levels[v] =0
  q.append(v)

  while q:
    j = q.pop(0)
    for k in AList[j]:
      if(not visited[k]):
        visited[k] = True
        parent[k] =j
        levels[k] = levels[j] + 1
        q.append(k)
  return(visited,parent,levels)

def BFS_ShortestPath(AList, start,end):
  (visited, parent, levels) = ({},{},{})
  for i in range(max(AList.keys())+1):
    visited[i] = False
    parent[i] = -1
    levels[i] = -1
  q = []
  visited[start] = True
  levels[start] =0
  q.append(start)

  while q:
    j = q.pop(0)
    for k in AList[j]:
      if(not visited[k]):
        visited[k] = True
        parent[k] =j
        levels[k] = levels[j] + 1
        q.append(k)

  path = []
  path.append(end)
  route = parent[end]
  while route!= -1:
     path.append(route)
     route = parent[route]
  
  return(path[::-1])


start=7
end=1
A = {0: [1, 4], 1: [2], 2: [0], 3: [4, 6], 4: [0, 3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
#print(BFS_ShortestPath(A,start,end))


visited = BFS(A,start)
print('BFS')
print(f'Visited List:{visited} from {start}')

'''
(visited,parent) = BFS_Path(A,start)
print('BFS path')
#print(f'Visited List:{visited} from {start}')
print(f'Parent List:{parent} from {start}')


(visited,parent,levels) = BFS_PathLevels(A,start)
print('BFS Path Levels')
#print(f'Visited List:{visited} from {start}')
print(f'Parent List:{parent} from {start}')
print(f'Levels List:{levels} from {start}')

''' 







  '''
# RECURSIVE WORK IN PROGRESS
def BFS_recursive_modified(A, start, end):
  
    # Actual BFS recursive Function
    def BFS_r(destination):
        if not Q:
            return
        
        node = Q.pop(0)
        if node == destination:
            return 

        if not visited[node]:
            visited[node] = True
            for neighbor in A[node]:
                if not visited[neighbor]:
                    Q.append(neighbor)
                    parent[neighbor] = node
        
        BFS_r(destination)
        return 

    # Setup Environment
    Q = [start]
    visited = {i: False for i in range(max(A.keys())+1)}
    parent = {i: -1 for i in range(max(A.keys())+1)}

    BFS_r(end)
 
    return (visited, parent)

# Testing the modified BFS_recursive function
#A = {0: [1, 4], 1: [2], 2: [0], 3: [4, 6], 4: [0, 3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
#print(BFS_recursive_modified(A, 7, 1))
'''