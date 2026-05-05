"""
main.py
=======
Main entry point for the Graph Search Engine.

Executes BFS, DFS, and IDDFS algorithms on a configured graph
and displays results with visualization.

Author: Graph Search Engine Team
Version: 1.0.0
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search
from iterative_deepening_search import iterative_deepening_search
from graph_visualizer import visualize_graph


# ============================================================
# GRAPH CONFIGURATION
# ============================================================

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

ROOT_NODE = "A"
MAX_DEPTH = 2  # Depth of the tree (A -> B -> D/E or A -> C -> F/G)

# ============================================================
# EXECUTION
# ============================================================

def main():
    """Execute all search algorithms and display results."""
    print("\n" + "=" * 60)
    print("🔍 GRAPH SEARCH ENGINE — Uninformed Search Algorithms")
    print("=" * 60)
    print(f"Graph: Binary Tree with 7 nodes (A–G)")
    print(f"Root:  {ROOT_NODE}")
    print(f"Depth: {MAX_DEPTH}")
    print("=" * 60)

    # BFS
    bfs_result = breadth_first_search(GRAPH, ROOT_NODE)
    print(f"\n📊 BFS (Breadth-First Search):")
    print(f"   Visitation Order: {bfs_result}")

    # DFS
    dfs_result = depth_first_search(GRAPH, ROOT_NODE)
    print(f"\n📊 DFS (Depth-First Search):")
    print(f"   Visitation Order: {dfs_result}")

    # IDDFS
    iddfs_result = iterative_deepening_search(GRAPH, ROOT_NODE, MAX_DEPTH)
    print(f"\n📊 IDDFS (Iterative Deepening DFS):")
    for depth, order in iddfs_result.items():
        print(f"   Depth {depth}: {order}")

    print("\n" + "=" * 60)
    print("✅ Search Complete")
    print("=" * 60)

    # Visualize
    visualize_graph(GRAPH, "Binary Tree — Uninformed Search Test Graph")


if __name__ == "__main__":
    main()