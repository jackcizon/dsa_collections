from collections import deque

from dsa_collections.ds.tree import BinaryTree


def _del_sub_trees(t: BinaryTree, node: "BinaryTree._TreeNode"):
    if node:
        _del_sub_trees(t, node.left)
        _del_sub_trees(t, node.right)


def search_del_x(t: BinaryTree, x):
    if t.is_empty():
        return

    curr = t._root

    if curr.key == x:
        _del_sub_trees(t, curr)
        return

    q = deque([curr])
    while q:
        node = q.popleft()

        if node.left:
            if node.left.key == x:
                _del_sub_trees(t, node.left)
                node.left = None
            else:
                q.append(node.left)

        if node.right:
            if node.right.key == x:
                _del_sub_trees(t, node.right)
                node.right = None
            else:
                q.append(node.right)
