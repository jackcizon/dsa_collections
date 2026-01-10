from dataclasses import dataclass
from typing import Any, Optional, Hashable, Iterator


class HashTable:
    """HashTable implementation via Python dict style perturbation probing"""

    @dataclass(repr=False, slots=True)
    class _Entry:
        hash: int
        key: Hashable
        value: Any
        is_deleted: bool = False

    def __init__(self, exp2_len: int = 4) -> None:
        if exp2_len < 2:
            exp2_len = 2
        self._size = 2**exp2_len
        self._count = 0  # active entries
        self._used = 0  # active + tombstone
        self._entries: list[Optional[HashTable._Entry]] = [None] * self._size

    def size(self) -> int:
        return self._size

    @staticmethod
    def _hash(key: Hashable) -> int:
        return hash(key)

    def _reach_limit(self) -> bool:
        """check hashtable usage"""
        return self._load_factor() > 0.5 or self._used_factor() > 0.667

    def _load_factor(self) -> float:
        """active entries proportion of usage"""
        return self._count / self._size

    def _used_factor(self) -> float:
        """active and tombstone entries proportion of usage"""
        return self._used / self._size

    def _resize(self) -> None:
        # save old
        old_entries: list["HashTable._Entry"] = self._entries
        # re-size
        self._size *= 2
        self._entries = [None] * self._size
        self._count = 0
        self._used = 0

        # re-insert
        for entry in old_entries:
            if entry and entry.is_deleted is False:
                self.insert(key=entry.key, value=entry.value)

    def insert(self, key: Hashable, value: Any) -> bool:
        if self._reach_limit():
            self._resize()

        h = self._hash(key)
        mask = self._size - 1
        idx = h & mask
        perturb = h
        first_tombstone = None

        # quad probe
        while True:
            entry: Optional["HashTable._Entry"] = self._entries[idx]

            # not exists, insert new
            if entry is None:
                # all probes get None, insert into first tombstone
                if first_tombstone is not None:
                    idx = first_tombstone
                self._entries[idx] = self._Entry(hash=h, key=key, value=value)
                self._count += 1
                self._used += 1
                return True

            # tombstone, entry is softly deleted, but we need probe next
            if entry.is_deleted and first_tombstone is None:
                first_tombstone = idx

            # if exists, overwrite
            if entry and entry.is_deleted is False and entry.hash == h and entry.key == key:
                entry.value = value
                return False

            # next probe
            idx = (idx * 5 + perturb + 1) & mask
            perturb >>= 5

    def delete(self, key: Hashable) -> bool:
        h = self._hash(key)
        mask = self._size - 1
        idx = h & mask
        perturb = h

        # quad probe
        while True:
            entry: Optional["HashTable._Entry"] = self._entries[idx]

            if entry is None:
                return False

            if entry.is_deleted is False and entry.hash == h and entry.key == key:
                entry.is_deleted = True
                self._count -= 1
                return True

            idx = (idx * 5 + perturb + 1) & mask
            perturb >>= 5

    def update(self, key: Hashable, value: Any) -> bool:
        h = self._hash(key)
        mask = self._size - 1
        idx = h & mask
        perturb = h

        while True:
            entry: Optional["HashTable._Entry"] = self._entries[idx]

            if entry is None:
                return False

            if entry.is_deleted is False and entry.hash == h and entry.key == key:
                entry.value = value
                return True

            idx = (idx * 5 + perturb + 1) & mask
            perturb >>= 5

    def get(self, key: Hashable) -> Any:
        h = self._hash(key)
        mask = self._size - 1
        idx = h & mask
        perturb = h

        while True:
            entry: Optional["HashTable._Entry"] = self._entries[idx]

            if entry is None:
                return None

            if entry.is_deleted is False and entry.hash == h and entry.key == key:
                return entry.value

            idx = (idx * 5 + perturb + 1) & mask
            perturb >>= 5

    def keys(self) -> Iterator:
        for entry in self._entries:
            if entry is not None and entry.is_deleted is False:
                yield entry.key

    def values(self) -> Iterator:
        for entry in self._entries:
            if entry is not None and not entry.is_deleted:
                yield entry.value

    def items(self) -> Iterator:
        for entry in self._entries:
            if entry is not None and not entry.is_deleted:
                yield entry.key, entry.value

    def __contains__(self, key: Hashable) -> bool:
        return self.get(key) is not None

    def __len__(self) -> int:
        return self._count

    def __iter__(self) -> Iterator:
        yield self.keys()
