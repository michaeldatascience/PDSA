'''
The express train routes are provided in the adjacency list `AList`, here you have to find the route from `start` to `end` with minimum number of hops possible. Write a function `minimumhops(AList, start, end)` to return the cities to be visited starting from `start` to `end`. Return a list with only `start` if the `end` is not reachable.

**Sample Input**
```python
start = 8
end = 7
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
```

**Sample returned list**
```python
[8, 9, 1, 3, 7]
```
**Sample output**
```python
5
```
**Graphical representation**
'''

'''
BFS algo start with start, end with 7 and traversal list returned

'''


def minimumhops(AList, start, end):
    '''
    BFS algo, store the visited path and return
    '''
    # Initialize visited list with False and count = length of Adjacency List
    visited = [False for _ in range(max(AList.keys()) + 1 )]
    parent = [-1 for _ in range (max(AList.keys())+1)]
    Q = []
    Q.append(start)
    Path = []
    
    while Q:
        node = Q.pop(0)
        if node == end:
            break

        visited[node]=True
        
        for sibling in AList[node]:
            if not visited[sibling]:
                parent[sibling] = node
                visited[sibling]= True
                Q.append(sibling)

    while end != -1:
        Path.append( end )
        end = parent[end]
    
    print(Path)
    return Path
#start = int(input())
#end = int(input())
#AList = eval(input())

start = 5
end = 1
AList = {1: [3, 2, 7], 2:[7,5], 3: [6,2], 5: [2], 6: [1], 7: [6]}

shortestpath = minimumhops(AList, start, end)
print(len(shortestpath))
