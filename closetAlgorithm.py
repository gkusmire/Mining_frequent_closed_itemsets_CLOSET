from Mining_frequent_closed_itemsets_CLOSET.fptreeBuilder import FPTreeBuilder
from Mining_frequent_closed_itemsets_CLOSET.frequent_closed_itemset import FrequentItemsetItem, FrequentClosedItemset


class ClosetFCIFinder:
    def __init__(self, file_name, min_support):
        fptree_builder = FPTreeBuilder(file_name, min_support)
        self.dictionary = fptree_builder.dictionary
        self.tree = fptree_builder.get_fptree()
        self.fci = FrequentClosedItemset(min_support)
        self.min_supp = min_support

    def build_frequent_closed_itemset(self):
        if self.tree is None:
            return self.fci

        frequent_items = self.tree.frequentItems
        items_in_every_transaction = self.tree.items_in_every_transaction

        self.closet_algorithm(items_in_every_transaction, self.tree, frequent_items)
        return self.fci

    def closet_algorithm(self, candidate_frequent_itemset, tree, f_list):
        self.fci.try_add(candidate_frequent_itemset)

        self.fci.print(self.dictionary)

        for item in f_list.items[::-1]:
            subtree = tree.get_subtree_associated_with(item, self.min_supp)
            frequent_itemset = self.get_candidate_frequent_itemset(candidate_frequent_itemset, item,
                                                                   subtree.items_in_every_transaction)
            subset_f_list = subtree.frequentItems

            self.closet_algorithm(frequent_itemset, subtree, subset_f_list)

    def get_candidate_frequent_itemset(self, itemset, item, item_list):
        # print(self.dictionary.dictionary[item.name])
        new_itemset = FrequentItemsetItem()
        new_itemset.copy_values(itemset)
        new_itemset.add(item.name, item.frequent_counter)
        for x in item_list.itemset:
            new_itemset.add(x, item_list.frequency)
        return new_itemset
