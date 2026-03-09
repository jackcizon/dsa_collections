"""
Portions of this file are derived from NetworkX
https://networkx.org

Original license: BSD 3-Clause License
Modifications Copyright (c) 2026 Jack Cizon
"""

import heapq
from collections import deque
from itertools import count
from typing import Hashable, Iterator

from dsa_collections.ds.graph import Graph


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

    Computes the shortest distances from a source node to all other nodes
    in a weighted graph with non-negative edge weights. Optionally, it can
    stop early when a specific target node is reached.

    Algorithm logic:
    1. init distance of the source to 0 and other nodes to inf(or check u in distance)
    2. use min-heap to repeatedly select the unvisited node with the min distance.
    3. for selected node, loop neighbors to update predecessors, visited and distance
    4. join node into set `visited`.
    5. repeat steps 2-4 until all visited, got target node finalized.

    Notes:
    - The algo maintains predecessors for building paths, but does not construct paths itself.

    e.g.:
        # from A to all:
        distance = {'A': 0, 'B': 2, 'C': 1, 'E': 3, 'D': 5, 'F': 5, 'G': 8, 'H': 6}
        predecessors = {'B': 'A', 'C': 'A', 'E': 'C', 'D': 'B', 'F': 'E', 'G': 'D', 'H': 'F'}

        # from A to H:
        distance = {'H': 6}
        predecessors = {'H': 'F', 'F': 'E', 'E': 'C', 'C': 'A'}


    :param graph: graph instance
    :param source: source node
    :param target: target node or None
    :return: tuple[dict, dict]
    """
    distance: dict[Hashable, float] = {source: 0}
    predecessors: dict[Hashable, Hashable] = {}
    visited: set = set()

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

            # similar to set distance[u] = inf, but we use `if u in distance`
            if u not in distance or min_dist_vu < distance[u]:
                distance[u] = min_dist_vu
                predecessors[u] = v  # update pred
                heapq.heappush(min_heap, (min_dist_vu, next(counter), u))  # pop min_val later

    if target is not None:
        if target not in distance:
            raise KeyError(f"No path to {target}")
        # only get the related pred part between source and target
        # predecessors = {
        #     'B': 'A',
        #     'C': 'A',
        #     'E': 'C',
        #     'D': 'B',
        #     'F': 'E',
        #     'G': 'D',
        #     'H': 'F'
        # }
        # this is a dict algo used to get the sub-graph struct
        curr = target
        filtered_target_predecessors = {}
        while curr != source:
            pred = predecessors[curr]
            filtered_target_predecessors[curr] = pred
            curr = pred
        # filtered_predecessors = {
        #     'C': 'A',
        #     'E': 'C',
        #     'F': 'E',
        #     'H': 'F'
        # }
        return {target: distance[target]}, filtered_target_predecessors
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
