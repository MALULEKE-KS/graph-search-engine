"""
iterative_deepening_search.py
=============================
Iterative Deepening Depth-First Search (IDDFS) implementation.

IDDFS combines the space efficiency of DFS with the completeness of BFS
by repeatedly performing depth-limited DFS with increasing depth limits.

Characteristics:
    - Complete: Yes (for finite graphs)
    - Optimal: Yes (for unweighted graphs)
    - Time Complexity: O(b^d)
    - Space Complexity: O(d)

Author: Graph Search Engine Team
Version: 1.0.0
"""

from typing import Dict, List


def _depth_limited_search(
    graph: Dict[str, List[str]],
    node: str,
    depth_limit: int,
    visited: List[str]
) -> None:
    """
    Recursive depth-limited search helper.

    Args:
        graph: Adjacency list representation
        node: Current node being explored
        depth_limit: Remaining depth allowed
        visited: List tracking visitation order
    """
    if depth_limit < 0:
        return

    visited.append(node)

    if depth_limit == 0:
        return

    for neighbor in graph.get(node, []):
        _depth_limited_search(graph, neighbor, depth_limit - 1, visited)


def iterative_deepening_search(
    graph: Dict[str, List[str]],
    start: str,
    max_depth: int
) -> Dict[int, List[str]]:
    """
    Perform Iterative Deepening Depth-First Search on a graph.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node for traversal
        max_depth: Maximum depth limit for the search

    Returns:
        Dictionary mapping each depth level to its visitation order

    Raises:
        ValueError: If start node is not in the graph
    """
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")

    result = {}

    for depth in range(max_depth + 1):
        visited = []
        _depth_limited_search(graph, start, depth, visited)
        result[depth] = visited

    return result