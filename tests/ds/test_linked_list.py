import pytest

from ds.linked_list import SingleLinkedList


def test_single_lined_list():
    linked_list = SingleLinkedList()

    linked_list.push(1)
    linked_list.push(0)

    linked_list.append("hello")
    linked_list.append("world")

    with pytest.raises(NotImplementedError):
        linked_list.insert()

    val = linked_list.pop()
    assert val == "world"

    with pytest.raises(NotImplementedError):
        linked_list.delete()

    print(list(linked_list))

    linked_list.pop()
    linked_list.pop()
    linked_list.pop()
    linked_list.pop()
