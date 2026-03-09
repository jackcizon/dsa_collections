import pytest

from dsa_collections.ds.dynamic_array import DynamicArray


def test_init():
    arr = DynamicArray(4)
    assert arr.size == 0
    assert arr.capacity == 4


def test_insert_end():
    arr = DynamicArray(2)
    arr.insert(1, 0)
    arr.insert(2, 1)

    assert arr.size == 2
    assert arr.get(0) == 1
    assert arr.get(1) == 2


def test_insert_front():
    arr = DynamicArray(4)
    arr.insert(1, 0)
    arr.insert(2, 0)
    arr.insert(3, 0)

    assert arr.size == 3
    assert arr.get(0) == 3
    assert arr.get(1) == 2
    assert arr.get(2) == 1


def test_insert_middle():
    arr = DynamicArray(4)
    arr.insert(1, 0)
    arr.insert(3, 1)
    arr.insert(2, 1)

    assert [arr.get(i) for i in range(arr.size)] == [1, 2, 3]


def test_resize():
    arr = DynamicArray(2)
    arr.insert(1, 0)
    arr.insert(2, 1)
    arr.insert(3, 2)  # 触发扩容

    assert arr.capacity == 4
    assert arr.size == 3
    assert arr.get(2) == 3


def test_delete_front():
    arr = DynamicArray(4)
    for i in range(4):
        arr.insert(i, i)

    arr.delete(0)

    assert arr.size == 3
    assert [arr.get(i) for i in range(arr.size)] == [1, 2, 3]


def test_delete_middle():
    arr = DynamicArray(5)
    for i in range(5):
        arr.insert(i, i)

    arr.delete(2)

    assert arr.size == 4
    assert [arr.get(i) for i in range(arr.size)] == [0, 1, 3, 4]


def test_delete_end():
    arr = DynamicArray(4)
    for i in range(4):
        arr.insert(i, i)

    arr.delete(3)

    assert arr.size == 3
    assert arr.get(2) == 2


def test_remove_existing_value():
    arr = DynamicArray(4)
    arr.insert(1, 0)
    arr.insert(2, 1)
    arr.insert(3, 2)

    result = arr.remove(2)

    assert result is True
    assert arr.size == 2
    assert not arr.exists(2)


def test_remove_non_existing_value():
    arr = DynamicArray(4)
    arr.insert(1, 0)

    result = arr.remove(99)

    assert result is False
    assert arr.size == 1


def test_get_valid_index():
    arr = DynamicArray(2)
    arr.insert(10, 0)

    assert arr.get(0) == 10


def test_get_invalid_index():
    arr = DynamicArray(2)

    with pytest.raises(IndexError):
        arr.get(0)


def test_exists():
    arr = DynamicArray(3)
    arr.insert("a", 0)
    arr.insert("b", 1)

    assert arr.exists("a") is True
    assert arr.exists("c") is False


def test_repeated_delete_front():
    arr = DynamicArray(100)
    for i in range(50):
        arr.insert(i, i)

    for _ in range(25):
        arr.delete(0)

    assert arr.size == 25
    assert arr.get(0) == 25


def test_is_empty():
    arr = DynamicArray(1)
    assert arr.is_empty() is True


def test_append_push_pop():
    arr = DynamicArray(1)
    arr.append(10)
    arr.append(9)
    arr.append(8)
    arr.push(11)
    arr.pop()

    assert arr.items[0] == 11
    assert arr.items[arr.size - 1] == 9


def test_check_index_insert():
    arr = DynamicArray(1)
    arr.append(10)
    arr.append(9)
    arr.append(8)

    with pytest.raises(IndexError):
        arr.insert(val=100, index=100)

    with pytest.raises(IndexError):
        arr.insert(val=10000, index=-1)


def test_iter():
    arr = DynamicArray(1)
    arr.append(10)
    arr.append(9)
    arr.append(8)
    print(list(arr))
