"""
graph_visualizer.py
===================
Graph visualization utility using NetworkX and Matplotlib.

Renders directed graph representations of search trees for
visual analysis of traversal patterns.

Author: Graph Search Engine Team
Version: 1.0.0
"""

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List


def visualize_graph(
    graph: Dict[str, List[str]],
    title: str = "Graph Representation"
) -> None:
    """
    Render and display a directed graph visualization.

    Args:
        graph: Adjacency list representation of the graph
        title: Title for the visualization window
    """
    G = nx.DiGraph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.figure(figsize=(6, 5))
    pos = nx.spring_layout(G, seed=42)  # Fixed seed for consistent layout

    nx.draw(
        G, pos,
        with_labels=True,
        node_color='#2563EB',
        node_size=2000,
        font_size=12,
        font_weight='bold',
        font_color='white',
        arrows=True,
        arrowstyle='-|>',
        arrowsize=20,
        edge_color='#6B7280'
    )

    plt.title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()