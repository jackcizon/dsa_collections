from ds.tree import BinarySearchTree, AVLTree


def test_binary_search_tree():
    tree = BinarySearchTree(key=1, data=1)

    assert tree.delete(1) is True
    assert tree.delete(1) is False
    assert tree.height() == 0
    tree.create_or_update(1, 1)
    tree.create_or_update(1, 1)
    assert tree.delete(1) is True
    assert tree.get(1) is None

    assert tree.min() is None
    assert tree.max() is None

    assert tree.predecessor(1) is None
    assert tree.successor(1) is None

    tree.insert(1, 1)
    tree.insert(4, 4)
    tree.insert(2, 2)
    tree.insert(3, 3)
    tree.insert(8, 8)
    tree.insert(5, 5)
    tree.insert(9, 9)
    tree.insert(8.5, {})

    tree.create_or_update(key=8.5, data=8.5)
    assert tree.get(key=8.5) == 8.5

    assert tree.predecessor(1) is None
    assert tree.predecessor(1) is None
    assert tree.successor(1).key == 2
    assert tree.predecessor(2).key == 1
    assert tree.successor(9) is None
    assert tree.predecessor(5).key == 4
    assert tree.predecessor(8).key == 5
    assert tree.successor(8.5).key == 9

    print(list(tree))
    assert tree.inorder() == [1, 2, 3, 4, 5, 8, 8.5, 9]
    assert tree.preorder() == [1, 4, 2, 3, 8, 5, 9, 8.5]
    assert tree.postorder() == [3, 2, 5, 8.5, 9, 8, 4, 1]
    assert tree.inorder_recursion() == [1, 2, 3, 4, 5, 8, 8.5, 9]

    assert tree.is_empty() is False
    assert tree.max().key == 9
    assert tree.min().key == 1
    assert tree.get(9) == 9
    assert tree.height() == 5

    assert tree.delete(100000) is False  # del none exists node
    assert tree.delete(8.5) is True  # del leaf
    tree.insert(8.5, 8.5)
    assert tree.delete(9) is True  # del: node has 1 child: left
    tree.insert(9, 9)
    assert tree.delete(2) is True  # del: node has 1 child: right
    tree.insert(2, 2)
    assert tree.delete(9) is True
    assert tree.delete(4) is True  # del: node has 2 children
    tree.insert(4, 4)

    assert tree.get(9) is None

    print(list(tree))

    tree1 = BinarySearchTree(1, 1)
    # node2 = BinarySearchTree._TreeNode(2, 2)
    node0 = BinarySearchTree._TreeNode(0, 0)
    tree1._root.left = node0
    tree1._is_leaf(tree1._root.left)
    tree1.delete(0)
    tree1.create_or_update(2, 2)
    tree1.create_or_update(0, 0)
    assert tree1.insert(1, 1) is False
    tree1.delete(1)
    tree1.delete(2)
    tree1.delete(0)
    assert tree1._is_leaf(tree1._root) is False


def test_avl_tree():
    tree = AVLTree(key=1, data=1)
    print(tree)
