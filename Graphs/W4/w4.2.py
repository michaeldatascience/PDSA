def uniquepaths(paths):
    visited = set()
    for path in paths:
        for i in path:
            visited.add(i)
            

def backandforth_v2(AList, start, end):
    paths = []

    def dfs(node, currentpath, end, visited):
        visited.append(node)
        if node == end:
            paths.append(currentpath.copy())
            currentpath.pop()
            return
        
        for neighbor in AList[node]:
            if neighbor not in visited:
                dfs(neighbor, currentpath + [neighbor], end, visited.copy())  # passing a copy of visited list
                
    dfs(start, [start], end, [])  # start with an empty visited list

    print(paths)
    return len(paths)


end1 = 8
end2 = 4

AList = {0: [1, 4], 1: [2], 2: [0], 3: [4, 6], 4: [0, 3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}

output_v2 = backandforth_v2(AList, end1, end2)
print(output_v2)
