import networkx as nx
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

AList = {
    0: [8],
    8: [0, 9],
    1: [3, 5, 8],
    3: [1, 7, 2],
    5: [4],
    2: [8, 9],
    9: [1],
    7: [8],
    4: [2, 6],
    6: [9]
}

start = 8
end = 0

def BFS(AList, start, end):
    visited = [False for _ in range(max(AList.keys()) + 1)]
    queue = [[start]]
    visited[start] = True

    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == end:
            return path
        
        for neighbor in AList[node]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None

def visualize_graph(AList, path=None):
    G = nx.Graph()

    for node, neighbors in AList.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
            
    pos = nx.spring_layout(G) 
    nx.draw_networkx_nodes(G, pos, node_size=1000)
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos)
    
    if path:
        nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], width=2, edge_color='r')
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r', node_size=1000)
    
    plt.title("Graph Visualization")
    plt.show()

def on_button_click(b):
    clear_output(wait=True)
    display(button)
    
    path = BFS(AList, start, end)
    if path:
        print(f"The shortest path from {start} to {end} is: {path}")
        visualize_graph(AList, path)
    else:
        print(f"There is no path from {start} to {end}")
        visualize_graph(AList)

button = widgets.Button(description="Find Shortest Path")
button.on_click(on_button_click)
display(button)
