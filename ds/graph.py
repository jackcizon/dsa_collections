# This Graph and DiGraph implementation is a lightweight adaptation inspired by NetworkX
# Original NetworkX classes are licensed under the BSD 3-Clause License
# (https://networkx.org)
# Heavily modified and rewritten by Jack Cizon


from typing import Any, Hashable, Optional, Iterator, Union, overload, Literal


class Graph:
    """
    Graph is a pure data structure.
    It does NOT implement algorithms.
    Algorithms operate on Graph via public interfaces only.

    the graph class in networkx lib is a dict that stores JSON data.
    therefore, the graph instance is a dict.
    vertex is hashable, but not class.
    Almost all graph libs do not use class/struct to define vertex.

    _graph = {
        'name': 'AAA',
        # other attrs
    },
    _nodes = {
        # id: node attrs_dict
        1: {'label': 'S'},
        2: {'label': 'A'},
        3: {},
        ...
    },
    _adj: {
        # start: {neighbor_id: edge_attrs_dict}
        1: {
            2: {'weight': 2, 'label': 'road'},
            3: {'weight': 5}
        },
        2: {3: {'weight': 1}},
        ...
    }
    """

    def __init__(self, **attrs: Any):
        self._graph = {}
        self._nodes: dict[Hashable, dict[Hashable, Any]] = {}
        self._adj: dict[Hashable, dict[Hashable, Any]] = {}
        self._graph.update(attrs)

    def __getattr__(self, attr: str) -> Any:
        try:
            return self._graph[attr]
        except KeyError:
            raise AttributeError(attr)

    @property
    def name(self) -> Optional[str]:
        """return graph name"""
        return self._graph.get("name", "")

    def add_node(self, node: Hashable, **attrs: Any) -> None:
        """
        G.add_node(1, (size=10))
        :param node:
        :return:
        """
        if node not in self._nodes:
            self._adj[node] = {}  # clear node adj info
            self._nodes[node] = dict(attrs)  # set node attrs
        else:  # update attrs if node exists
            self._nodes[node].update(attrs)

    def add_edge(self, u: Hashable, v: Hashable, **attrs: Any) -> None:
        """
        G.add_edge(1, 3, (weight=7, capacity=15, length=342.7))

        _adj ={
            1: {
                2: {'weight': 5, 'label': 'road'},
                3: {}
            },
            2: {
                3: {'weight': 1}
            }
        }

        :param u:
        :param v:
        # :param weight:
        :return:
        """
        if u not in self._nodes:
            # reset node and adj info
            self._nodes[u] = {}
            self._adj[u] = {}

        if v not in self._nodes:
            self._nodes[v] = {}
            self._adj[v] = {}

        # add edge
        # if u, v first connect, {u: v: {}, ...}
        u2v_attrs = self._adj[u].get(v, {})
        u2v_attrs.update(attrs)
        # update edges info
        self._adj[u][v] = u2v_attrs
        self._adj[v][u] = u2v_attrs

    def remove_node(self, node: Hashable) -> None:
        adj = self._adj
        try:
            node_neighbor_keys: list[Hashable] = list(adj[node])  # get snapshot, not itself
            del self._nodes[node]
        except KeyError:
            raise KeyError(f"node {node} is not in the graph")
        for neighbor in node_neighbor_keys:
            # del self._adj[neighbor][node], will cause error
            del adj[neighbor][node]
        del self._adj[node]

    def remove_edge(self, u: Hashable, v: Hashable) -> None:
        try:
            del self._adj[u][v]
            if u != v:  # self-loop needs only one entry removed
                del self._adj[v][u]
        except KeyError:
            raise KeyError(f"edge: [{u}-{v}] is not in the graph")

    @staticmethod
    def is_directed() -> bool:
        return False

    def nodes(self) -> list:
        return list(self._nodes)

    def number_of_nodes(self) -> int:
        return len(self._nodes)

    def __iter__(self) -> Iterator:
        return iter(self._nodes)

    def __len__(self) -> int:
        """return number of nodes"""
        return self.number_of_nodes()

    def clear(self) -> None:
        self._adj.clear()
        self._nodes.clear()
        self._graph.clear()

    def has_node(self, node: Hashable) -> bool:
        if node in self._nodes:
            return True
        return False

    def has_edge(self, u: Hashable, v: Hashable) -> bool:
        try:
            return v in self._adj[u] and u in self._adj[v]
        except KeyError:
            return False

    def neighbors(self, node: Hashable) -> Optional[dict]:
        try:
            return self._adj[node]
        except KeyError:
            raise KeyError(f"node {node} is not in the graph")

    def neighbors_keys(self, node: Hashable) -> list:
        neighbors_dict = self.neighbors(node)
        return list(dict(neighbors_dict).keys()) if neighbors_dict else []

    @overload
    def edges(
        self, need_attrs: Literal[True] = True
    ) -> list[tuple[Hashable, Hashable, dict[Hashable, Any]]]:
        """get edges with edge attrs info"""
        ...

    @overload
    def edges(self, need_attrs: Literal[False]) -> list[tuple[Hashable, Hashable]]:
        """get edges without edge attrs info"""
        ...

    def edges(self, need_attrs: bool = True) -> list[Any]:
        """return all edges, with(out) attrs distinctly."""
        seen = set()
        edge_list = []
        for u, neighbors in self._adj.items():
            for v, attrs in neighbors.items():
                if (v, u) not in seen:  # 去掉重复
                    edge_list.append((u, v, attrs) if need_attrs else (u, v))
                    seen.add((u, v))
        return edge_list

    def get_edge_data(self, u: Hashable, v: Hashable) -> Optional[dict]:
        try:
            return self._adj[u][v]
        except KeyError:
            raise KeyError(f"edge [{u}-{v}] is not in the graph")

    def number_of_edges(self) -> int:
        return len(self.edges(need_attrs=False))

    def adjacency(self) -> list:
        return list(self._adj.items())

    def degree(self, node: Optional[Hashable] = None) -> Union[dict[Hashable, int], int]:
        if node is None:
            return {u: len(neighbors) for u, neighbors in self._adj.items()}
        return len(self._adj.get(node, {}))


class DGraph(Graph):
    """Directed Graph"""

    # def is_directed(self) -> bool:
    #     return True
