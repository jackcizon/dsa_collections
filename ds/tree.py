from dataclasses import dataclass
from typing import Any, Optional, Iterator


class BinaryTree:
    @dataclass(repr=False)
    class _TreeNode:
        key: float
        data: Any
        left: Optional["BinaryTree._TreeNode"] = None
        right: Optional["BinaryTree._TreeNode"] = None

    def __init__(self, key: float, data: Any) -> None:
        self._root = self._TreeNode(key=key, data=data, left=None, right=None)

    def is_empty(self) -> bool:
        return self._root is None

    def get(self, key: float) -> Optional[_TreeNode]:
        if self.is_empty():
            return None

        curr = self._root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr
        return None


class BinarySearchTree(BinaryTree):
    @dataclass(repr=False)
    class _TreeNode(BinaryTree._TreeNode):
        left: Optional["BinarySearchTree._TreeNode"] = None
        right: Optional["BinarySearchTree._TreeNode"] = None

    def __init__(self, key: float, data: Any = None) -> None:
        # super().__init__(key=key, data=data)
        # it will cause incompatible type "ds.tree.BinaryTree._TreeNode";
        # expected "ds.tree.BinarySearchTree._TreeNode | None"
        super().__init__(key, data)
        self._root: Optional[BinarySearchTree._TreeNode] = self._TreeNode(key=key, data=data)

    def min(self) -> Optional[_TreeNode]:
        """return leftmost node"""
        return self._min(self._root)

    def _min(self, node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        if self.is_empty():
            return None

        while node.left:
            node = node.left
        return node

    def max(self) -> Optional[_TreeNode]:
        """return rightmost node"""
        return self._max(self._root)

    def _max(self, node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        if self.is_empty():
            return None

        while node.right:
            node = node.right
        return node

    def __iter__(self) -> Iterator:
        stack: list[BinarySearchTree._TreeNode] = []
        curr = self._root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            yield curr.data
            curr = curr.right

    def preorder(self) -> list:
        """root, left, right"""
        stack = [self._root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def postorder(self) -> list:
        """left, right, root"""
        stack = [self._root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return list(reversed(result))

    def inorder_recursion(self) -> list:
        return self._inorder_recursion(self._root, [])

    def _inorder_recursion(self, root: Optional[_TreeNode], result: list) -> list:
        """left, root, right"""
        if root is None:
            return []
        self._inorder_recursion(root.left, result)
        result.append(root.data)
        self._inorder_recursion(root.right, result)
        return result

    def inorder(self) -> list:
        """
        left, root, right
        find leftmost, continue push, util finish left child tree,
        then switch to right child tree, loop
        """
        curr = self._root
        stack: list[BinarySearchTree._TreeNode] = []
        result = []

        # loop
        while curr or stack:
            # find leftmost, push all nodes in the path
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.data)
            # switch to right child tree
            curr = curr.right

        return result

    def create_or_update(self, key: float, data: Any = None) -> None:
        if self.is_empty():
            self._root = self._TreeNode(key=key, data=data)
            return

        curr = self._root
        parent = None

        while curr:
            parent = curr

            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                curr.data = data  # found, update
                return

        # cannot find, create new
        node = self._TreeNode(key=key, data=data)
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def insert(self, key: float, data: Any = None) -> bool:
        if self.is_empty():
            self._root = self._TreeNode(key=key, data=data)
            return True

        curr = self._root
        parent = None

        while curr:
            parent = curr

            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return False  # key exists

        # key does not exist, create new
        node = self._TreeNode(key=key, data=data)
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node
        return True

    def predecessor(self, key: float) -> Optional[_TreeNode]:
        """
        1. left child tree -> max(curr.left)
                or
        2. curr.left is None -> find from ancestor, left part < curr
        """
        if self.is_empty():
            return None

        ancestor_from_left = None
        curr = self._root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                ancestor_from_left = curr
                curr = curr.right
            else:
                break

        if curr.left:
            return self._max(curr.left)
        return ancestor_from_left

    def successor(self, key: float) -> Optional[_TreeNode]:
        """
        1. right child tree -> min(curr.right)
                or
        2. curr.right is None -> find from ancestor, right > curr

        Based on the mathematical symmetry of binary trees,
        the left and right subtrees are symmetrical,
        and the predecessor and successor nodes are also symmetrical.
        """
        if self.is_empty():
            return None

        ancestor_from_right = None
        curr = self._root

        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                ancestor_from_right = curr
                curr = curr.left
            else:
                break

        if curr.right:
            return self._min(curr.right)
        return ancestor_from_right

    def _is_leaf(self, node: Optional[_TreeNode]) -> bool:
        if self.is_empty():
            return False
        return node.left is None and node.right is None

    def _shift(
        self,
        parent: Optional[_TreeNode],
        deleted: _TreeNode,
        child: Optional[_TreeNode],
    ) -> None:
        if parent is None:
            self._root = child
        elif deleted is parent.left:
            parent.left = child
        else:
            parent.right = child

    def delete(self, key: float) -> bool:
        if self.is_empty():
            return False

        curr = self._root
        parent = None

        # find node
        while curr:
            if key < curr.key:
                parent = curr
                curr = curr.left
            elif key > curr.key:
                parent = curr
                curr = curr.right
            else:
                break

        deleted = curr

        # key does not exist
        if deleted is None:
            return False

        # key found, is leaf(maybe single root), it's parent's left or right child
        if self._is_leaf(deleted):
            self._shift(parent=parent, deleted=deleted, child=None)
            return True

        # key found, has left or right child, not both
        if deleted.left is None and deleted.right is not None:
            self._shift(parent=parent, deleted=deleted, child=deleted.right)
            return True
        if deleted.right is None and deleted.left is not None:
            self._shift(parent=parent, deleted=deleted, child=deleted.left)
            return True

        # key found, but has 2 children, must base on inorder iteration
        # left(child_tree) < root < right(child_tree)
        # to find the successor to replace deleted node
        # because successor(may be has right child tree) and all remaining nodes  > curr
        # can not be predecessor, because curr(deleted node) has right(child tree)
        # which will violate BST invariant
        # find successor and its parent
        successor: BinarySearchTree._TreeNode = deleted.right
        successor_parent = deleted

        while successor.left:
            successor_parent = successor
            successor = successor.left

        # curr(deleted) not adjacent with successor
        # and successor maybe has right(child tree) possibly
        # must solve successor things
        if successor_parent != deleted:
            self._shift(parent=successor_parent, deleted=successor, child=successor.right)
            successor.right = deleted.right

        # curr(deleted) adjacent with successor
        self._shift(parent=parent, deleted=deleted, child=successor)
        successor.left = deleted.left
        return True

    def height(self) -> int:
        return self._height_recursion(self._root)

    def _height_recursion(self, node: Optional[_TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height_recursion(node.left), self._height_recursion(node.right))


class AVLTree(BinaryTree):
    """self balanced binary search tree"""

    @dataclass(repr=False)
    class _TreeNode(BinaryTree._TreeNode):
        height: int = 1
        left: Optional["AVLTree._TreeNode"] = None
        right: Optional["AVLTree._TreeNode"] = None

    def __init__(self, key: float, data: Any = None) -> None:
        super().__init__(key, data)
        self._root: Optional[AVLTree._TreeNode] = self._TreeNode(key=key, data=data)

    @staticmethod
    def _height(node: Optional[_TreeNode]) -> int:
        if node is None:
            return 0
        return node.height

    def _update_height(self, node: Optional[_TreeNode]) -> None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: Optional[_TreeNode]) -> int:
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        r"""
        left-rotate the node and related node:
            its right child becomes the new root of this subtree,
            and the node becomes the left child of the new root.
        in the case of left rotation, the tree is right-leaning.

        e.g.:
               5
             /   \
            3     6
           / \     \
          2   4    (7) <- (delete(7) causes violation)
         /
        1
               5
             /   \
            3     6
           / \
          2   4
         /
        (1) <- (insert(1) causes violation)
        """
        if node is None or node.right is None:
            return node  # can't rotate

        right_child = node.right
        right_child_left = right_child.left
        # rotate
        node.right = right_child_left
        right_child.left = node
        # update height
        self._update_height(node)
        self._update_height(right_child)
        # other methods need the new root to maintain avl-tree invariant
        return right_child

    def _right_rotate(self, node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        """
        it's symmetrical to left rotate.
        in the case of right rotation, the tree is left-leaning.

        e.g.:
            mirror of left_rotate()
        """
        # normal tests cannot cover this guard, because delete() logic
        if node is None or node.left is None:  # pragma: no cover
            return node

        left_child = node.left
        left_child_right = left_child.right
        node.left = left_child_right
        left_child.right = node
        self._update_height(node)
        self._update_height(left_child)
        return left_child

    def _left_right_rotate(self, node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        r"""
        perform a left rotation on node's left, followed by a right rotation on node.
        returns the new root of the subtree.

        e.g.:
               6
             /   \
            2     7
           / \     \
          1   4    (9) <- (delete(9) causes violation)
             / \
            3   5
        """
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _right_left_rotate(self, node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        """
        it's symmetrical to left right rotate.
        perform a left rotation on node's left, followed by a right rotation on node.
        returns the new root of the subtree.

        e.g.:
            mirror of left_right_rotate()
        """
        node.right = self._left_rotate(node.right)
        return self._left_rotate(node)

    def _balance(self, node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        """
        helper method to maintain avl-tree invariant after insertion and deletion.

        if the subtree is already balanced, the original node is returned.
        if rotations are required, returns the new root of this subtree.
        """
        # defensive guard that will not happen in normal situations
        if node is None:  # pragma: no cover
            return None
        bf = self._balance_factor(node)

        # 1. Left-Left:
        # height(z.left) - height(z.right) = 2, bf = 2
        # height(z.left.left) >= height(z.left.right), bf >= 0
        # aka LL
        if bf > 1 and self._balance_factor(node.left) >= 0:
            return self._right_rotate(node)
        # 2. LR
        # the complement of case 1
        elif bf > 1 and self._balance_factor(node.left) < 0:
            return self._left_right_rotate(node)
        # 3. Right-Right
        # height(z.right) - height(z.left) = 2, bf = -2
        # height(z.right.right) >= height(z.right.left), bf <= 0
        # aka RR
        elif bf < -1 and self._balance_factor(node.right) <= 0:
            return self._left_rotate(node)
        # 4. RL
        # the complement of case 3
        elif bf < -1 and self._balance_factor(node.right) > 0:
            return self._right_left_rotate(node)

        return node

    def insert_or_update(self, key: float, data: Any = None) -> None:
        """insert new node or update if exists"""
        self._root = self._insert_recursion(node=self._root, key=key, data=data)

    def _insert_recursion(
        self, node: Optional[_TreeNode], key: float, data: Any
    ) -> Optional[_TreeNode]:
        """inner method, insert recursively"""
        # empty avl-tree
        if node is None:
            return self._TreeNode(key=key, data=data)

        # key exists, update node data
        if key == node.key:
            node.data = data
            return node

        # key not found, insert recursively
        if key < node.key:
            node.left = self._insert_recursion(node=node.left, key=key, data=data)
        else:
            node.right = self._insert_recursion(node=node.right, key=key, data=data)

        # update nodes height, maintain avl-tree invariant
        self._update_height(node)
        return self._balance(node)

    @staticmethod
    def _get_min_node(node: Optional[_TreeNode]) -> Optional[_TreeNode]:
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key: float) -> None:
        self._root = self._delete_recursion(node=self._root, key=key)

    def _delete_recursion(self, node: Optional[_TreeNode], key: float) -> Optional[_TreeNode]:
        # empty avl-tree
        if node is None:
            return None

        # delete recursively
        if key < node.key:
            node.left = self._delete_recursion(node=node.left, key=key)
        elif key > node.key:
            node.right = self._delete_recursion(node=node.right, key=key)
        else:
            # key found
            if node.left is None:
                return node.right  # 0/1 child
            elif node.right is None:
                return node.left  # 1 child
            else:
                # 2 children, find successor(min in right subtree)
                successor = self._get_min_node(node.right)
                # copy data
                node.key = successor.key
                node.right = self._delete_recursion(node=node.right, key=successor.key)

        # update nodes height, maintain avl-tree invariant
        self._update_height(node)
        return self._balance(node)

    def __iter__(self) -> Iterator:
        stack: list[AVLTree._TreeNode] = []
        curr = self._root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            yield curr.data
            curr = curr.right


class RBTree(BinaryTree):
    pass
