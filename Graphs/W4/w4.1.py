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


def minimumhops(Alist, start, end):
    # Initialization
    visited = [False] * (max(Alist.keys()) + 1)  # Adjusted for the number of nodes
    previous = {}  # To keep track of the path
    queue = [start]
    visited[start] = True
    
    while queue:
        v = queue.pop(0)
        
        # If we've reached the end node, we can break
        if v == end:
            break
        
        for neighbor in Alist[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                previous[neighbor] = v  # Store where we came from
                queue.append(neighbor)

    # Reconstruct the shortest path
    path = []
    while end in previous:
        path.append(end)
        end = previous[end]
    path.append(start)
    
    return path[::-1]  # Reverse the path to get from start to end



# Suffix Code
start = int(input())
end = int(input())
AList = eval(input())
shortestpath = minimumhops(AList, start, end)
print(len(shortestpath))
