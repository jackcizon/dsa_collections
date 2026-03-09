from dsa_collections.ds.tree import BinarySearchTree, AVLTree, RBTree


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
    assert tree.get(key=8.5).key == 8.5

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
    assert tree.get(9).key == 9
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


def test_avl_tree_rotations_simple():
    # 初始化 AVL 树
    tree = AVLTree(key=10, data=10)  # data = key

    tree.delete(10)
    tree.delete(1000)

    tree.insert_or_update(key=10, data=0)
    tree.insert_or_update(key=10, data=10)

    # ---------------------
    # 插入触发各种旋转
    # ---------------------

    # LL case: 左左旋（右旋）
    tree.insert_or_update(5, 5)
    tree.insert_or_update(2, 2)  # 插入左左 → 右旋
    values = list(tree)
    assert values == [2, 5, 10]

    # RR case: 右右旋（左旋）
    tree.insert_or_update(15, 15)
    tree.insert_or_update(20, 20)  # 插入右右 → 左旋
    values = list(tree)
    assert values == [2, 5, 10, 15, 20]

    # LR case: 左右旋（左旋 + 右旋）
    tree.insert_or_update(4, 4)  # 插入 4 → LR
    values = list(tree)
    assert values == [2, 4, 5, 10, 15, 20]

    # RL case: 右左旋（右旋 + 左旋）
    tree.insert_or_update(17, 17)  # 插入 17 → RL
    values = list(tree)
    assert values == [2, 4, 5, 10, 15, 17, 20]

    # ---------------------
    # 删除触发旋转
    # ---------------------

    # 删除叶子和中间节点，可能触发旋转
    tree.delete(20)  # 删除右右叶子节点
    tree.delete(2)  # 删除左左叶子节点
    tree.delete(17)  # 删除右左节点
    tree.delete(4)  # 删除左右节点

    # 最后中序遍历应该剩下 [5,10,15]
    values = list(tree)
    assert values == [5, 10, 15]

    ##############################################
    # test some lines that are hard to trigger
    ##############################################

    # test _left_right_rotate()
    tree2 = AVLTree(6)
    tree2.insert_or_update(2)
    tree2.insert_or_update(7)
    tree2.insert_or_update(1)
    tree2.insert_or_update(4)
    tree2.insert_or_update(9)  # del this node will trigger LR
    tree2.insert_or_update(3)
    tree2.insert_or_update(5)
    tree2.delete(9)

    # test _get_min_node()
    tree3 = AVLTree(4)  # del this node
    tree3.insert_or_update(2)
    tree3.insert_or_update(6)  # node.right
    tree3.insert_or_update(1)
    tree3.insert_or_update(3)
    tree3.insert_or_update(5)  # successor of 4
    tree3.insert_or_update(7)
    tree3.insert_or_update(5.5)
    tree3.delete(4)


def test_rb_tree():
    # insert
    r"""
    case 0: root
    15(black)
    """
    tree1 = RBTree()
    tree1.insert_or_update(15)

    r"""
    case 3:
    node.uncle = black(line)
    rotate(node.grandpa)
    recolor parent and grandpa
            15(black)                                  5(b)
           /       \                   fix_up         /   \
          5(red)    nil <- uncle      -------->     1(r) 15(r)
         /                             recolor
        1 <- insert
    """
    tree2 = RBTree()
    tree2.insert_or_update(15)
    tree2.insert_or_update(5)
    tree2.insert_or_update(1)

    r"""
    case 1:
    node.uncle = red
    recolor parent, grandpa and uncle
    iteration node.grandpa
             |                                      |
            12(b)                                 12(r)
            /   \               recolor           /   \
          9(r) 13(r)          ---------->        9(b) 13(b) 
           \                                      \
           10(r)                                  10(r)  
    """
    tree3 = RBTree()
    tree3.insert_or_update(12)
    tree3.insert_or_update(9)
    tree3.insert_or_update(13)
    tree3.insert_or_update(10)

    r"""
    case 2:
    triangle
    node.uncle = black
    rotate node.parent
                     8(b)       \
                   /      \      \
         uncle -> 5(b)   15(r)   /
                         /      /
              node ->  12(r)   /
    """
    tree4 = RBTree()
    tree4.insert_or_update(8)
    tree4.insert_or_update(5)
    tree4.insert_or_update(15)
    tree4.insert_or_update(12)
    tree4.insert_or_update(19)
    tree4.insert_or_update(9)
    tree4.insert_or_update(13)
    tree4.insert_or_update(23)
    tree4.insert_or_update(10)
