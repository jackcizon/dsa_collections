# Some algorithms in this library are inspired by NetworkX
# (https://networkx.org)
# but implementations have been independently rewritten.

"""
Graph algorithms.

All functions here:
- operate on ds.graph.Graph
- do NOT modify graph structure
"""

import heapq
from collections import deque
from itertools import count, islice
from typing import Hashable, Iterator, Any

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


def dijkstra(graph: Graph, source: Hashable, target: Hashable | None = None) -> tuple[dict, dict]:
    """
    single source min path algo.

    :param graph: graph instance
    :param source: source node
    :param target: target node or None
    :return: tuple[dict, dict]
    """
    distance: dict[Hashable, float] = {source: 0}
    predecessors: dict[Hashable, Hashable] = {}
    visited: set = set()
    # paths: dict[Hashable, list[Hashable]] = {source: [source]}

    # node: Hashable may cannot compare, it will cause MinHeap compare error,
    # so we need a counter: Iterable to increment by 1 each call to make the
    # heap val can be compared. heap like:
    # min_heap: list[tuple[int, int, Hashable]] = MinHeap([(weight, counter, node), ...])
    counter = count()
    min_heap: list[tuple[int, int, Hashable]] = []
    heapq.heappush(min_heap, (0, next(counter), source))  # init min heap

    while min_heap:
        # tuple unpack: distance, counter(useless) -> _, node
        dist_v, _, v = heapq.heappop(min_heap)
        if v in visited:
            continue
        visited.add(v)

        # loop neighbors, we can get the full distance
        for u, attrs in graph[v].items():
            weight = graph.weight(v, u)
            min_dist_vu = dist_v + weight

            if u not in distance or min_dist_vu < distance[u]:  # similar to inf, but we use if u in distance
                distance[u] = min_dist_vu
                predecessors[u] = v  # update pred
                heapq.heappush(min_heap, (min_dist_vu, next(counter), u))  # push in heap, get min val after

    # build paths, before this, we have already got distance
    # build paths operation is not the core of dijkstra algo
    # the core is (predecessors, distance)
    # it's python list skill representation
    # for node in distance:
    #     if node == source:
    #         continue
    #     path = []
    #     current = node
    #     while current != source:
    #         path.append(current)
    #         current = predecessors[current]
    #     path.append(source)
    #     path.reverse()
    #     paths[node] = path

    if target is not None:
        if target not in distance:
            raise KeyError(f"No path to {target}")
        # return {target: distance[target]}, {target: paths[target]}
        return {target: distance[target]}, predecessors

    # return distance, paths
    return distance, predecessors

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
