"""
Recursive List.

see `Router` implementation in `./example/recursive_list_example.py`
"""

from typing import Any


class RListElement:
    pass


class RListNode(RListElement):
    def __init__(self, value: Any) -> None:
        self.value = value


class RListPointer(RListElement):
    def __init__(self, value: Any, rlist: "RList") -> None:
        self.value = value
        self.rlist = rlist


class RList:
    def __init__(self) -> None:
        self._elements: list[RListElement] = []

    def add_node(self, value: Any) -> None:
        rlist_node = RListNode(value)
        self._elements.append(rlist_node)

    def add_list(self, rlist: "RList", value: Any) -> None:
        rlist_ptr = RListPointer(value, rlist)
        self._elements.append(rlist_ptr)

    def elements(self, base: Any = None) -> list[Any]:
        _elements = []
        for element in self._elements:
            if isinstance(element, RListNode):
                _elements.append(f"{base} -> {element.value}")
            elif isinstance(element, RListPointer):
                nodes = element.rlist.elements(f"{base} -> {element.value}")
                _elements.extend(nodes)
        return _elements
