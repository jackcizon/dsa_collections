import pytest

from dsa_collections.ds.graph import Graph


def test_graph():
    g = Graph(name="g1", author="jack")
    assert g.name == "g1"
    assert g.author == "jack"
    with pytest.raises(AttributeError):
        print(g.aaa)

    g.bb = "1"

    print("\n\ngraph_info =", g._graph)

    print("\n# before inserting:")
    print("adj =", g._adj)
    print("nodes =", g._nodes)

    g.add_node(1)
    g.add_node(1, color="red")
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)

    g.add_edge(1, 2, weight=2)
    g.add_edge(4, 5)
    g.add_edge(6, 6)
    g.add_edge(7, 8)  # when 7, 8 are not in _nodes

    print("\n# after inserting:")
    print("adj1 =", g._adj)
    print("nodes1 =", g._nodes)

    g.remove_node(3)
    g.remove_edge(4, 5)
    g.remove_edge(6, 6)
    g.remove_node(6)
    g.remove_node(7)
    with pytest.raises(KeyError):
        g.remove_node("non-exist-node")
    with pytest.raises(KeyError):
        g.remove_edge("non-1", "non-2")

    print("\n# after deleting:")
    print("adj2 =", g._adj)
    print("nodes2 =", g._nodes)

    assert g.is_directed() is False

    assert list(g._nodes) == g.nodes()
    assert g.number_of_nodes() == len(g)

    assert g.has_node("") is False
    assert g.has_node(5) is True
    assert g.has_edge("1", "3") is False
    assert g.has_edge(1, 2) is True

    assert (2 in g.neighbors(1).keys()) is True
    with pytest.raises(KeyError):
        g.neighbors("none-exists-node")
    assert (2 in g.neighbors_keys(1)) is True
    with pytest.raises(KeyError):
        g.neighbors_keys(-100)

    assert g.get_edge_attrs(1, 2) == {"weight": 2}
    with pytest.raises(KeyError):
        g.get_edge_attrs("n1", "n2")

    assert g.edges() == [(1, 2, {"weight": 2})]
    assert g.edges(need_attrs=False) == [(1, 2)]
    assert len(g.edges(need_attrs=False)) == g.number_of_edges() == 1
    assert g.adjacency == {1: {2: {"weight": 2}}, 2: {1: {"weight": 2}}, 4: {}, 5: {}, 8: {}}

    print("\n# __getitem__ test:")
    print("g[1] =", g[1])
    print("g[1][2] =", g[1][2])

    assert g.degree() == {1: 1, 2: 1, 4: 0, 5: 0, 8: 0}
    assert g.degree(node=1) == 1

    assert g.weight(1, 2) == 2  # true
    g.add_edge(1, 2, weight=1)  # update weight
    assert g.weight(1, 2) == 1  # true
    assert g.get_edge_attrs(1, 2)["weight"] == 1
    with pytest.raises(KeyError):
        g.weight(10000, 100)

    g.update_edge_attrs(1, 2, weight=10)
    assert g.weight(1, 2) == 10
    with pytest.raises(KeyError):
        g.update_edge_attrs(100, 1000, aaa=1)

    assert g.get_node_attrs(1) == {"color": "red"}
    g.update_node_attrs(1, color="black", name="1")
    assert g.get_node_attrs(1) == {"color": "black", "name": "1"}
    with pytest.raises(KeyError):
        g.get_node_attrs(-100)
    with pytest.raises(KeyError):
        g.update_node_attrs(-1000)

    g.reset_node_attrs(1)
    assert g.get_node_attrs(1) == {}
    with pytest.raises(KeyError):
        g.reset_node_attrs(-100)

    g.reset_edge_attrs(1, 2)
    assert g.get_edge_attrs(1, 2) == {}
    with pytest.raises(KeyError):
        g.reset_edge_attrs(100, -100)

    assert (1 in g) is True
    assert (-99999 in g) is False

    print("\n# after operations:")
    print("adj2 =", g._adj)
    print("nodes2 =", g._nodes)

    print("total nodes list =", list(g))
    g.clear()
    print("\nafter clearing:")
    print("g =", list(g))
