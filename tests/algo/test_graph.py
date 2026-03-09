import pytest

from dsa_collections.ds.graph import Graph
from dsa_collections.algo.graph import dfs, bfs, dijkstra


def make_graph():
    r"""
    1---2-----6----7--\
    |\  |          |__|
    | \ |
    |  \|               100 (isolated node is not conclude)
    3---4-----5
    """
    g = Graph(name="test_dfs")
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 7)
    g.add_node(100)
    return g


def test_dfs():
    g = make_graph()
    assert list(dfs(graph=g, source=1)) == [1, 4, 5, 3, 2, 6, 7]
    assert list(dfs(graph=g, source=100)) == [100]


def test_bfs():
    g = make_graph()
    assert list(bfs(graph=g, source=1)) == [1, 2, 3, 4, 6, 5, 7]
    assert list(bfs(graph=g, source=100)) == [100]


def test_dijkstra():
    # 1️⃣ 构建图
    g = Graph(name="g1", author="jack")

    g.add_edge("A", "B", weight=2)
    g.add_edge("A", "C", weight=1)
    g.add_edge("B", "D", weight=3)
    g.add_edge("C", "E", weight=2)
    g.add_edge("D", "F", weight=1)
    g.add_edge("E", "F", weight=2)
    g.add_edge("A", "E", weight=4)
    g.add_edge("D", "E", weight=2)
    g.add_edge("D", "G", weight=3)
    g.add_edge("G", "H", weight=2)
    g.add_edge("D", "H", weight=4)
    g.add_edge("F", "H", weight=1)

    r"""
      2   3   3
    A---B---D---G
    |\4    /|\4 |
   1| \   / | \ |2
    |  \ /2 |1 \|
    C---E---F---H
      2   2   1
    """

    # distances, paths = dijkstra(g, source="A")
    # print("\n# from A to all:")
    # print("distance:", distances)
    # print("paths:", paths)

    distances, predecessors = dijkstra(g, source="A")
    print("\n# from A to all:")
    print("distance =", distances)
    print("predecessors =", predecessors)

    # distance, path = dijkstra(g, source="A", target="H")
    # print("\n# from A to H:")
    # print("distance:", distance)
    # print("paths:", path)
    distance, predecessors = dijkstra(g, source="A", target="H")
    print("\n# from A to H:")
    print("distance =", distance)
    print("target_predecessors =", predecessors)

    with pytest.raises(KeyError):
        dijkstra(g, source="A", target=-1000)
