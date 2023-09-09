from graphviz import Digraph

def generate_graph_from_adj_list(adj_list):
    dot = Digraph(comment='Graph from Adjacency List')
    
    # Add nodes to the graph
    for node in adj_list.keys():
        dot.node(str(node))
    
    # Add edges to the graph
    for node, neighbors in adj_list.items():
        for neighbor, weight in neighbors:
            dot.edge(str(node), str(neighbor), label=str(weight))
    
    return dot


A = {
    0: [(1, 10), (2, 50), (3, 300)],
    1: [(0, 10), (2, 30), (6, 65), (3, 40)],
    2: [(0, 50), (1, 30), (5, 76), (4, 20)],
    3: [(0, 300), (1, 40), (4, 60)],
    4: [(6, 37), (3, 60), (2, 20)],
    5: [(6, 45), (2, 76)],
    6: [(5, 45), (4, 37), (1, 65)]
}


def kruskal(WList):
    # List to store edges, dictionary to store component of each vertex, and list to store tree edges (TE)
    edges = []
    component = {}
    TE = []

    # Convert adjacency list to a list of edges and initialize each vertex's component to itself
    for u in WList:
        edges.extend([(d, u, v) for (v, d) in WList[u]])
        component[u] = u

    # Sort edges based on their weights for Kruskal's algorithm
    edges.sort()

    # Process edges in increasing order of their weights
    for (d, u, v) in edges:
        # If the endpoints belong to different components, add the edge to the MST
        if component[u] != component[v]:
            TE.append((u, v))
            old_component = component[u]
            
            # Merge the components of u and v
            for w in component:
                if component[w] == old_component:
                    component[w] = component[v]

    return TE



graph = generate_graph_from_adj_list(A)
graph.view()
print(kruskal(A))