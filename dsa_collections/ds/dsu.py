class DSU:
    """
    DSU is It is typically used to store index relationships like:
    1. parent-child relationships in SQL,
    2. tree-like parent-child relationships
    3. ID values of nodes in a graph.
    """

    def __init__(self, size: int):
        """
        By default, -1 represents the root of the tree;
        initially, each node is an independent tree.

        :param size: int
        """
        self.s = [-1] * size

    def find(self, x: int) -> int:
        """
        Iteratively search until the root (value < 0) is returned.

        :param x: value
        :return: int
        """
        while self.s[x] > 0:
            x = self.s[x]
        return x

    def union(self, a: int, b: int):
        """
        Steps:
        1. Find the roots of a and b.

        2. If they have the same root, return False.

        3. A root stores a negative value.
           Its absolute value represents the number of nodes in the set.

        4. The root of the larger set remains the root.
           Add the size of the smaller set to it
           (both values are negative),
           then make the smaller root point to the larger root.

        5. Update the parent index of the smaller root.
        """
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.s[b] > self.s[a]:
            self.s[a] += self.s[b]
            self.s[b] = a
        else:
            self.s[b] += self.s[a]
            self.s[a] = b
