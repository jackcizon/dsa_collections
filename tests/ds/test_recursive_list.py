from dsa_collections.ds.recursive_list import RList


class TestRList:
    def test_operations(self):
        rlist_1 = RList()
        rlist_1.add_node("1")
        rlist_1.add_node("2")

        rlist_1_1 = RList()
        rlist_1_1.add_node("3")
        rlist_1_1.add_node("4")
        rlist_1.add_list(rlist_1_1, "rlist_1_1")

        rlist_ = RList()
        rlist_.add_list(rlist_1, "rlist_1")

        for element_ in rlist_.elements():
            print(element_)
