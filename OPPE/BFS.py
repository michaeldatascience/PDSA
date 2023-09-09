def AllInOne(AList, start, end):
  # returns shortest path between start and end
  # distance between levels of start and 
  visited,parent,levels = {},{},{}
  path = []
  for i in range(len(AList)):
    visited[i]= False
    parent[i]= -1
    levels[i]= -1

  visited[start] = True
  levels[start] = 0

  Q = [start]
  while Q:
    nextV = Q.pop(0)
    for neighbor in AList[nextV]:
      if not visited[neighbor]:
        visited[neighbor] = True
        parent[neighbor] = nextV
        levels[neighbor] = levels[nextV] + 1
        Q.append(neighbor)
    
  # Path
  while end!= -1:
    path.append(end)
    end = parent[end]

  return (path)


  




def leveldiff(Alist, start, end):
  # sampe code for level difference between two nodes
  parents,visited,levels = {},{},{}
  paths=[]
  for i in range(len(AList)):
    parents[i] = -1
    visited[i] = False
    levels[i] = -1

  #Important step
  Q=[start]
  visited[start]=True
  levels[start]=0

  while (Q):
    nextV = Q.pop(0)
    for neighbor in AList[nextV]:
      if not visited[neighbor]:
        visited[neighbor] = True
        parents[neighbor] = nextV
        levels[neighbor] = levels[nextV]  + 1
        Q.append(neighbor)
        
    # Level
  return (levels[end])



def minimumhops(Alist, start, end):
    # initialize all three, visitd, parents, levels
    (visited,parent,levels) = ({},{},{})
    path = []
    for i in range(len(AList)):
      visited[i] = False
      parent[i] = -1
      levels[i] = 0

    Q=[start]
    visited[start] = True
    
    while (Q):
      nextV = Q.pop(0)
      for neighbor in (Alist[nextV]):
        if not visited[neighbor]:
          visited[neighbor] = True
          parent[neighbor] = nextV
          # level of current is level of parent +1 
          levels[neighbor] = levels[nextV] + 1
          Q.append(neighbor)

    # back tracking parents dict from end till you get -1
    while end!=-1:
      path.append(end)
      # find the previous link (parent) of end
      end = parent[end]

    #Dont use sort!!!!
    path.reverse()
    return path




start = 8
end = 5
AList = {
            0: [8],
            8: [0, 9],
            1: [3, 5, 8],
            3: [1, 2, 7],
            5: [4],
            2: [8, 9],
            9: [1],
            7: [8],
            4: [2, 6],
            6: [9]
    }


#shortestpath = minimumhops(AList, start, end)
#print(f'shortestpath between {start} and {end}: {shortestpath}')

#levelDiff = leveldiff(AList,start,end)
#print(f'Level difference: {levelDiff}')

path1 = AllInOne(AList, start,end)

print(path1)

#print(minimumhops(AList,start,end))