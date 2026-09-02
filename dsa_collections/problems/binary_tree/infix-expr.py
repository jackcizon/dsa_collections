"""
给定的二叉树表达式树转化为中缀表达式
"""
from dsa_collections.ds.tree import BinaryTree


def infix_expr(T: BinaryTree, expr=None):
    if expr is None:
        expr = []

    _infix_expr(T._root, 1, expr)
    return expr


def _infix_expr(node: BinaryTree._TreeNode, depth, expr):
    if node is None:
        return None

    if node.left is None and node.right is None:
        expr.append(node.data)
        return

    if depth > 1:
        expr.append('(')

    _infix_expr(node.left, depth + 1, expr)
    expr.append(node.data)
    _infix_expr(node.right, depth + 1, expr)

    if depth > 1:
        expr.append(')')
