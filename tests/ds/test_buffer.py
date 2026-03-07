import pytest

from ds.buffer import Buffer


def test_init():
    size = 100
    b = Buffer(size)
    assert b.capacity == size
    assert b._data == bytearray(size)
    assert b._read_pos == 0
    assert b._write_pos == 0


def test_capacity():
    assert Buffer(10).capacity == 10


def test_readable_size():
    assert Buffer().readable_size == 0


def test_writeable_size():
    assert Buffer(10).writable_size == 10


def test_data():
    assert Buffer().data == ""


def test__is_buf_enough():
    b = Buffer(10)
    assert b._is_buf_enough(1) is True
    assert b._is_buf_enough(100) is False


def test__can_merge():
    b = Buffer(10)
    assert b._can_merge(9) is True
    assert b._can_merge(100) is False


def test__extend():
    size = 1
    ext = 2
    b = Buffer(size)
    b._extend(ext)
    assert b._data == bytearray(size + ext)
    assert b._capacity == size + ext


def test__try_extend():
    size = 5
    ext = 10
    b = Buffer(size)
    b._try_extend(ext)
    assert b._capacity == size + ext


def test_append():
    b1 = "1"
    b2 = "23456"
    size = 1
    buf = Buffer(size)
    buf.append("1")
    buf.append("23456")
    assert buf.data == f"{b1}{b2}"


def test_remove():
    with pytest.raises(NotImplementedError):
        Buffer().remove()


def test___str__():
    b3 = "123"
    buf = Buffer()
    buf.append(b3)
    assert buf.__str__() == b3


def test___iter__():
    l_b = ["1", "2", "3", "4"]
    b = "".join(l_b)
    buf = Buffer(100)
    buf.append(b)
    for index, s in enumerate(buf):
        assert s == l_b[index]
