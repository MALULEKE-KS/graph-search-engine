"""
breadth_first_search.py
=======================
Breadth-First Search (BFS) implementation for uninformed graph traversal.

BFS explores a graph level by level, visiting all neighbors at the current
depth before moving deeper. Guarantees the shortest path in unweighted graphs.

Characteristics:
    - Complete: Yes (for finite graphs)
    - Optimal: Yes (for unweighted graphs)
    - Time Complexity: O(V + E)
    - Space Complexity: O(V)

Author: Graph Search Engine Team
Version: 1.0.0
"""

from collections import deque
from typing import Dict, List


def breadth_first_search(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    Perform Breadth-First Search traversal on a graph.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node for traversal

    Returns:
        List of nodes in BFS visitation order

    Raises:
        ValueError: If start node is not in the graph
    """
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")

    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited