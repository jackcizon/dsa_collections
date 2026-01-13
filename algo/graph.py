# Some algorithms in this library are inspired by NetworkX
# (https://networkx.org)
# but implementations have been independently rewritten.

"""
Graph algorithms.

All functions here:
- operate on ds.graph.Graph
- do NOT modify graph structure
"""

from collections import deque
from typing import Hashable, Iterator

from ds.graph import Graph


def dfs(graph: Graph, source: Hashable) -> Iterator[Hashable]:
    """
    Perform a depth-first search (DFS) traversal starting from a source node.

    DFS is a graph traversal algorithm that explores nodes by going as deep
    as possible along each branch before backtracking. Each node reachable
    from the source is yielded exactly once. DFS uses a stack (LIFO) to
    manage the frontier and handles cycles and self-loops correctly.

    Key properties:
    - Traversal is depth-first (go deep before backtracking)
    - Single-source: only visits nodes reachable from `source`
    - Handles cycles and self-loops correctly
    - Uses a stack (LIFO) to manage frontier nodes

    :param graph: the graph instance
    :param source: the start node
    :return: Iterator of nodes
    """
    visited: set[Hashable] = {source}
    stack: list[Hashable] = [source]
    while stack:
        node = stack.pop()
        # visited.add(node)  # notes: this line is for those men who will make this mistake
        yield node
        for neighbor in graph.neighbors_keys(node):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)


def bfs(graph: Graph, source: Hashable) -> Iterator[Hashable]:
    """
    Perform a breadth-first search (BFS) traversal starting from a source node.

    BFS is a graph traversal algorithm that explores nodes layer by layer:
    it first visits all neighbors of the source node, then neighbors of neighbors,
    and so on, until all reachable nodes are visited.

    Key properties:
    - Traversal is level-order (layer by layer)
    - Single-source: only visits nodes reachable from `source`
    - Handles cycles and self-loops correctly
    - Uses a queue (FIFO) to manage frontier nodes

    :param graph: the graph instance
    :param source: the start node
    :return: Iterator of nodes
    """
    visited: set[Hashable] = {source}
    queue: deque[Hashable] = deque([source])
    while queue:
        node = queue.popleft()  # O(1), do not use list, it's O(n)
        yield node
        for neighbor in graph.neighbors_keys(node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


# def topo_sort(graph: Graph):
#     """
#     Notes:
#         must use directed graph
#     :param graph:
#     :return:
#     """
#     pass
#
#
# def dijkstra(graph: Graph):
#     pass
#
#
# def bellman_ford(graph: Graph):
#     pass
#
#
# def floyd_warshall(graph: Graph):
#     pass
#
#
# def mst_prim(graph: Graph):
#     pass
#
#
# def mst_kruskal(graph: Graph):
#     pass
