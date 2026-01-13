from ds.graph import Graph
from algo.graph import dfs


def test_dfs():
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

    r"""
    1---2-----6----7--\
    |\  |          |__|
    | \ |     
    |  \|               100 (isolated node is not conclude)
    3---4-----5
    """

    assert list(dfs(graph=g, source=1)) == [1, 4, 5, 3, 2, 6, 7]
    assert list(dfs(graph=g, source=100)) == [100]


def test_bfs():
    pass


# ......
