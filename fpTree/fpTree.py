from Mining_frequent_closed_itemsets_CLOSET.fpTree.fpTreeNode import Node


class FPTree:

    def __init__(self, frequent_items_):
        self.treeNode = Node("null", 0)
        self.frequentItems = frequent_items_
