# struct SqBiTree {
#   int SqBiNode[MAX_SIZE];
#   int Number;
# };


class SqBiTree:
    sqBiNode: list
    number: int


def is_bst(tree: SqBiTree):
    stack = [(0, float("-inf"), float("inf"))]

    while stack:
        i, low, high = stack.pop()

        if i >= tree.number:
            continue

        val = tree.sqBiNode[i]

        if val == -1:
            continue

        if val <= low or val >= high:
            return False

        stack.append((2 * i + 1, low, val))
        stack.append((2 * i + 2, val, high))

    return True
