class XYZ_Courier:
    def __init__(self, route_map):
            self.route_map = route_map

    #def cost(self, source, destination):

    def _dijkstra(self, s):
        print(self.route_map)
        WList = self.route_map
        # Determine maximum possible distance for initialization
        infinity = 1 + len(WList) * max(d for _, d in [item for sublist in WList.values() for item in sublist])
        
        # Initialize visited and distance dictionaries
        visited = {v: False for v in WList}
        distance = {v: infinity for v in WList}
        distance[s] = 0

        while True:
            # Get unvisited vertex with the shortest distance
            unvisited_distances = {v: d for v, d in distance.items() if not visited[v]}
            if not unvisited_distances:
                break
            nextv = min(unvisited_distances, key=unvisited_distances.get)

            # Mark as visited and update neighbor distances
            visited[nextv] = True
            for (v, d) in WList[nextv]:
                if not visited[v]:
                    distance[v] = min(distance[v], distance[nextv] + d)

        return distance

             
size = 7 #int(input())
edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)] #eval(input())
s= 0 #int(input())
d= 4 #int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
C = XYZ_Courier(WL)
#print(C.cost(s,d))
#print(C.route(s,d))
print(C._dijkstra(s))