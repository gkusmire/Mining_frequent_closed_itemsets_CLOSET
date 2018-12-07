from Mining_frequent_closed_itemsets_CLOSET.fpTree.fpTreeNode import Node
from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItem import FrequentItem


class FPTree:
    def __init__(self, frequent_items_):
        self.rootNode = Node(FrequentItem("null"))
        self.frequentItems = frequent_items_

    # TODO sorting of itemset
    def sort(self, itemset_):
        return itemset_

    def add_itemset(self, itemset):
        sorted_itemset = self.sort(itemset)
        actual_node = self.rootNode

        for item in sorted_itemset:
            element = self.frequentItems.get(item)

            if actual_node.get_children(element) is None:
                node = Node(element)

                if element.last_added_node is None:
                    element.last_added_node = node
                    element.node_link = node
                else:
                    element.last_added_node.node_link = node
                    element.last_added_node = node
                actual_node.add_children(node)
                actual_node.increment_counter()
                actual_node = node
            else:
                actual_node.increment_counter()
                actual_node = actual_node.get_children(element)
