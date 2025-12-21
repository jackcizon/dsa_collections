import pytest

from ds.linked_list import SingleLinkedList, DoubleLinkedList


def test_single_lined_list():
    linked_list = SingleLinkedList()

    linked_list.push(1)
    linked_list.push(0)

    linked_list.append("hello")
    linked_list.append("world")

    with pytest.raises(NotImplementedError):
        linked_list.insert()

    assert linked_list.pop() == "world"
    assert linked_list.pop_front() == 0

    with pytest.raises(NotImplementedError):
        linked_list.delete()

    print(list(linked_list))

    linked_list.pop()
    linked_list.pop()
    linked_list.pop()
    linked_list.pop_front()


def test_double_linked_list():
    linked_list = DoubleLinkedList()

    linked_list.is_empty()

    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.push(0)

    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)

    assert linked_list.pop_front() == 0
    assert linked_list.pop() == 6

    print(list(linked_list))
