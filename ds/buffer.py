from typing import Iterator


class Buffer:
    """a common ds for network programming."""

    def __init__(self, size: int = 4) -> None:
        self._capacity = size
        self._data = bytearray(self._capacity)
        self._read_pos = 0
        self._write_pos = 0

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def readable_size(self) -> int:
        """
        if the buffer has been partially read,
        the read portion can be replaced (written).
        the unread portion must be read first,
        and other operations can only be performed
        after the unread part is complete read.
        """
        return self._write_pos - self._read_pos

    @property
    def writable_size(self) -> int:
        return self._capacity - self._write_pos

    @property
    def data(self) -> str:
        return self._data[self._read_pos : self._write_pos].decode()

    def _is_buf_enough(self, size: int) -> bool:
        r"""
        (read=2)(  readable=3  )(    writeable=5    ) <<== incoming_size=4
        ---------------------------------------------
               /\              /\                  /\
               ||              ||                  ||
            r_pos=2         w_pos=5            capacity=10

        :param size: size of incoming buf
        """
        if self.writable_size > size:
            return True
        return False

    def _can_merge(self, size: int) -> bool:
        r"""
        before merging:
          //===can be replaced(writeable), because this portion has been read.
          ||
          \/
        (read=2)(  readable=3  )(    writeable=5    ) <<== incoming_size=6
        ---------------------------------------------
               /\              /\                  /\
               ||              ||                  ||
            r_pos=2         w_pos=5            capacity=10

        after merging:
        (readable=3)(          writeable=7          ) <<== incoming_size=6
        ---------------------------------------------
        /\         /\                              /\
        ||         ||                              ||
        r_pos=0  w_pos=3                      capacity=10

        switch to case ._buf_enough().

        :param size: size of incoming buf
        """
        if self._read_pos + self.writable_size >= size:
            readable_size = self.readable_size
            # mem copy
            copy_data = self._data[self._read_pos : self._write_pos]
            self._data[:readable_size] = copy_data
            # reset positions
            self._read_pos = 0
            self._write_pos = readable_size
            return True
        return False

    def _extend(self, size: int) -> None:
        self._data += bytearray(size)
        self._capacity += size

    def _try_extend(self, size: int) -> None:
        if self._is_buf_enough(size):
            return
        if self._can_merge(size):
            return
        self._extend(size)

    def append(self, buf: str) -> None:
        raw_buf = buf.encode()
        buf_size = len(raw_buf)
        self._try_extend(buf_size)
        self._data[self._write_pos : self._write_pos + buf_size] = raw_buf
        self._write_pos += buf_size

    def remove(self) -> None:
        """remove() method implementation is unnecessary."""
        raise NotImplementedError

    def __str__(self) -> str:
        return self.data

    def __iter__(self) -> Iterator:
        for s in self.data:
            yield s
