"""
depth_first_search.py
=====================
Depth-First Search (DFS) implementation for uninformed graph traversal.

DFS explores a graph by going as deep as possible along each branch before
backtracking. Uses less memory than BFS for deep graphs.

Characteristics:
    - Complete: No (can get stuck in infinite loops without cycle detection)
    - Optimal: No
    - Time Complexity: O(V + E)
    - Space Complexity: O(V)

Author: Graph Search Engine Team
Version: 1.0.0
"""

from typing import Dict, List


def depth_first_search(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    Perform Depth-First Search traversal on a graph.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node for traversal

    Returns:
        List of nodes in DFS visitation order

    Raises:
        ValueError: If start node is not in the graph
    """
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")

    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            # Reverse to maintain left-to-right traversal order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited