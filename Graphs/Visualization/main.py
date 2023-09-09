from flask import Flask, render_template, request
import networkx as nx
import plotly.graph_objects as go
from plotly.offline import plot

app = Flask(__name__)

# Sample graph
AList = {0: [8], 8: [0, 9], 1: [3, 5, 8], 3: [1, 7, 2], 5: [4], 2: [8, 9], 9: [1], 7: [8], 4: [2, 6], 6: [9]}
G = nx.Graph(AList)
pos = nx.spring_layout(G)

@app.route('/', methods=['POST', 'GET'])
def index():

    # For the initial display without path.
    edge_x = []
    edge_y = []
    for edge in G.edges():
        edge_x.extend([pos[edge[0]][0], pos[edge[1]][0], None])
        edge_y.extend([pos[edge[0]][1], pos[edge[1]][1], None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = [pos[node][0] for node in G.nodes()]
    node_y = [pos[node][1] for node in G.nodes()]

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2,
            color='#888'
        )
    )

    if request.method == 'POST':
        # Rest of the code
        start_node = int(request.form['start'])
        end_node = int(request.form['end'])

        shortest_path = shortest_path(G, start=start_node, end=end_node)

        edge_x = []
        edge_y = []
        path_edge_x = []
        path_edge_y = []
        for edge in G.edges():
            if edge in zip(shortest_path, shortest_path[1:]) or (edge[1], edge[0]) in zip(shortest_path, shortest_path[1:]):
                path_edge_x.extend([pos[edge[0]][0], pos[edge[1]][0], None])
                path_edge_y.extend([pos[edge[0]][1], pos[edge[1]][1], None])
            else:
                edge_x.extend([pos[edge[0]][0], pos[edge[1]][0], None])
                edge_y.extend([pos[edge[0]][1], pos[edge[1]][1], None])

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1, color='#888'),
            hoverinfo='none',
            mode='lines')

        path_edge_trace = go.Scatter(
            x=path_edge_x, y=path_edge_y,
            line=dict(width=2, color='red'),
            hoverinfo='none',
            mode='lines')

        node_x = [pos[node][0] for node in G.nodes()]
        node_y = [pos[node][1] for node in G.nodes()]

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2))

        node_colors = []
        for node in G.nodes():
            color = 'red' if node in shortest_path else '#888'
            node_colors.append(color)

        node_trace.marker.color = node_colors

        fig = go.Figure(data=[edge_trace, path_edge_trace, node_trace],
                     layout=go.Layout(
                        title='Network Graph made with Python',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        plot_div = plot(fig, output_type='div')
        return render_template('index.html', plot_div=plot_div)
    else:
        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='Network Graph made with Python',
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=0, l=0, r=0, t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        plot_div = plot(fig, output_type='div')
        return render_template('index.html', plot_div=plot_div)

if __name__ == "__main__":
    app.run(debug=True)
