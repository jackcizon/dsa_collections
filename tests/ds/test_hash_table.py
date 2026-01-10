from ds.hash_table import HashTable


def test_hashtable():
    """hash table test cov can barely reach 100%, unless with a amount of data and a small size"""
    print("=== HashTable Test ===")

    ht = HashTable(exp2_len=2)  # 小容量，测试扩容

    # --- 插入 ---
    assert ht.insert("a", 1) is True
    assert ht.insert("b", 2) is True
    assert ht.insert("c", 3) is True
    assert len(ht) == 3

    # --- 覆盖 ---
    assert ht.insert("b", 20) is False  # 覆盖返回 False
    assert ht.get("b") == 20

    # --- 更新 ---
    assert ht.update("c", 30) is True
    assert ht.get("c") == 30
    assert ht.update("x", 100) is False  # 不存在的 key

    # --- 删除 ---
    assert ht.delete("a") is True
    assert ht.get("a") is None
    assert ht.delete("a") is False  # 已经删除
    assert len(ht) == 2

    # --- contains ---
    assert "b" in ht
    assert "a" not in ht

    # --- 扩容 ---
    # 插入更多元素，触发 _resize
    for i in range(10):
        ht.insert(f"key{i}", i)
    assert len(ht) == 12  # 2 + 10
    for i in range(10):
        assert ht.get(f"key{i}") == i

    # --- 迭代 keys ---
    keys = set(ht.keys())
    expected_keys = {"b", "c"} | {f"key{i}" for i in range(10)}
    assert keys == expected_keys

    # --- 迭代 values ---
    values = set(ht.values())
    expected_values = {20, 30} | set(range(10))
    assert values == expected_values

    # --- 迭代 items ---
    items = set(ht.items())
    expected_items = {("b", 20), ("c", 30)} | {(f"key{i}", i) for i in range(10)}
    assert items == expected_items

    print(list(ht))

    print("All tests passed ✅")

    # test remaining part
    h = HashTable(-100)
    assert h.size() == 2**2
