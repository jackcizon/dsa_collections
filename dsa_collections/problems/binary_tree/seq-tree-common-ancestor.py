# struct SqBiTree {
#   int SqBiNode[MAX_SIZE];
#   int Number;
# };


class SqBiTree:
    sqBiNode: list
    number: int


def common_ancestor(t: SqBiTree, i: int, j: int):
    """
    空节点用'#'表示
    l = 2i + 1
    r = 2i + 2
    p = (k - 1) // 2
    """
    if t.sqBiNode[i] == '#' or t.sqBiNode[j] == '#':
        return None

    while i != j:
        if i > j:
            i = (i - 1) // 2
        else:
            j = (j - 1) // 2
    return t.sqBiNode[i]
