# Some algorithms in this library are inspired by NetworkX
# (https://networkx.org)
# but implementations have been independently rewritten.

"""
Graph algorithms.

All functions here:
- operate on ds.graph.Graph
- do NOT modify graph structure
"""

from typing import Hashable, Iterator

from ds.graph import Graph


def dfs(graph: Graph, source: Hashable) -> Iterator[Hashable]:
    """
    Depth First Search(DFS)

    a graph traversal algorithm that starts from a starting node:
    1. It first traverses a path to the end.
    2. then backtracks to the previous branch point, exploring other unvisited neighbors.
    3. This continues until all reachable nodes have been visited.
    4. if an isolated node is not a source node, it is simply not within the scope of dfs.

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


# def bfs(graph: Graph):
#     pass
#
#
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
