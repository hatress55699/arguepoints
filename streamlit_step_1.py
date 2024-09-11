# -*- coding: utf-8 -*-
"""
streamlit
Step 1: Create the Graph with Pyvis
"""

from pyvis.network import Network
import networkx as nx

# Create a NetworkX graph
G = nx.Graph()

# Define the nodes and edges as provided
data = {
    "nodes": [
        {"id": "A", "label": "A", "group": "Group 1"},
        {"id": "B", "label": "B", "group": "Group 1"},
        {"id": "C", "label": "C", "group": "Group 1"},
        {"id": "D", "label": "D", "group": "Group 1"},
        {"id": "KK", "label": "KK", "group": "Group 2"},
        {"id": "aa", "label": "aa", "group": "Group 3"},
        {"id": "qqa", "label": "qaa", "group": "Group 4"},
        {"id": "11", "label": "11", "group": "Group 3"}
    ],
    "edges": [
        {"source": "A", "target": "B", "weight": 1},
        {"source": "A", "target": "C", "weight": 1},
        {"source": "KK", "target": "B", "weight": 1},
        {"source": "KK", "target": "C", "weight": 1},
        {"source": "D", "target": "B", "weight": 1},
        {"source": "aa", "target": "KK", "weight": 1},
        {"source": "aa", "target": "11", "weight": 3},
        {"source": "KK", "target": "D", "weight": 1}  
    ]
}

# Define custom colors for each group, change colours https://www.w3schools.com/cssref/css_colors.php
group_colors = {
    "Group 1": "#FFE4C4",  
    "Group 2": "#FF8C00",  
    "Group 3": "#483D8B",  
    "Group 4": "##EE82EE"    
}

# Add nodes to the graph
for node in data["nodes"]:
    G.add_node(
        node["id"],
        label=node["label"],
        group=node["group"]
    )

# Add edges to the graph
for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"], weight=edge["weight"])

# Create a Pyvis network
net = Network(notebook=True)
net.from_nx(G)

# Update the colors directly in Pyvis
for node in net.nodes:
    node['color'] = group_colors.get(node['group'], "gray")  # Assign colors based on the group

# Customize the network (optional)
net.show_buttons(filter_=['physics'])

# Define the path where the HTML file will be saved
output_path = r"C:\Users\doya\Desktop\Python_stuff\reddit_visualisation\streamlit_network.html"

# Generate the network visualization and save it as an HTML file
net.save_graph(output_path)
