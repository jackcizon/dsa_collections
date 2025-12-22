import pytest

from ds.linked_list import SingleLinkedList, DoubleLinkedList, DoubleCircledLinkedList


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

    with pytest.raises(NotImplementedError):
        linked_list.insert()
    with pytest.raises(NotImplementedError):
        linked_list.delete()

    assert linked_list.pop() is None
    assert linked_list.pop_front() is None

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
    while not linked_list.is_empty():
        linked_list.pop()
    print(list(linked_list))


def test_double_circled_linked_list():
    linked_list = DoubleCircledLinkedList()

    linked_list.is_empty()

    with pytest.raises(NotImplementedError):
        linked_list.insert()
    with pytest.raises(NotImplementedError):
        linked_list.delete()

    assert linked_list.pop() is None
    assert linked_list.pop_front() is None

    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)

    assert linked_list.pop_front() == 1
    assert linked_list.pop() == 8

    print(list(linked_list))
    while not linked_list.is_empty():
        linked_list.pop()
    print(list(linked_list))
