from Mining_frequent_closed_itemsets_CLOSET.fpTree.fpTreeNode import Node
from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItem import FrequentItem
from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItemset import FrequentItemSet
from Mining_frequent_closed_itemsets_CLOSET.frequent_closed_itemset import FrequentItemsetItem


class FPTree:
    def __init__(self, frequent_items_):
        self.rootNode = Node(FrequentItem("null"))
        self.frequentItems = frequent_items_
        self.items_in_every_transaction = FrequentItemsetItem()

    def prepare(self, itemset):
        sorted_list = []
        for element in self.frequentItems.items:
            if element.name in itemset:
                sorted_list.append(element)

        return sorted_list

    def add_itemset(self, itemset):
        sorted_itemset = self.prepare(itemset)
        actual_node = self.rootNode

        for element in sorted_itemset:
            if actual_node.get_children(element) is None:
                node = Node(element)
                node.parent_link = actual_node
                actual_node.add_children(node)

                if element.last_added_node is None:
                    element.last_added_node = node
                    element.node_link = node
                else:
                    element.last_added_node.node_link = node
                    element.last_added_node = node
                actual_node.increment_counter()
                actual_node = node
            else:
                actual_node.increment_counter()
                actual_node = actual_node.get_children(element)
        actual_node.increment_counter()

    def extract_items_associated_in_every_transaction(self):
        if len(self.rootNode.childrenNodes) != 1:
            return
        if self.rootNode.counter != self.rootNode.childrenNodes[0].counter:
            return
        actual_node = self.rootNode.childrenNodes[0]

        if len(actual_node.childrenNodes) == 0:
            self.rootNode.childrenNodes.clear()
        else:
            self.rootNode.childrenNodes = actual_node.childrenNodes
            for node in actual_node.childrenNodes:
                node.parent_link = self.rootNode

        actual_node.parent_link = None
        self.items_in_every_transaction.add(actual_node.item.name, actual_node.item.frequent_counter)
        self.frequentItems.delete(actual_node.item)
        self.extract_items_associated_in_every_transaction()

    def print_tree(self, dictionary):
        print("LEVEL 0 NULL:", end='')
        print(self.rootNode.counter, end='')

        for level in range(1, 10):
            print("")
            print("LEVEL", end=' ')
            print(level, end=' ')
            self.print_level(level, self.rootNode, dictionary)

    def print_level(self, level, node, dictionary):
        if level == 0:
            print(dictionary.dictionary[node.item.name] + ":", end='')
            print(node.counter, end=' ')
        for x in node.childrenNodes:
            self.print_level(level-1, x, dictionary)

    def get_subtree_associated_with(self, item, min_supp):
        transactions = []
        frequent_itemset = self.get_frequent_sublist_and_transactions(item, transactions)
        subtree = FPTree(frequent_itemset)
        for x in transactions:
            subtree.add_itemset(x)
        subtree.extract_items_associated_in_every_transaction()
        return subtree

        # self.extract_items_associated_in_every_transaction()
    def get_frequent_sublist_and_transactions(self, item, transactions):
        frequent_items = FrequentItemSet()
        node = item.node_link
        while not(node is None):
            trans = []
            frequency = node.counter
            for x in range(frequency):
                trans.append([])
            transaction_it = node.parent_link

            while not(transaction_it.parent_link is None):
                frequent_items.add(transaction_it.item.name, frequency)
                for x in trans:
                    x.append(transaction_it.item.name)
                transaction_it = transaction_it.parent_link
            for x in trans:
                transactions.append(x)
            node = node.node_link
        frequent_items.sort_descending()
        return frequent_items
