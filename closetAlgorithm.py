from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItemset import FrequentItemSet


class ClosetFCIFinder:
    def __init__(self, frequent_pattern_tree, min_support):
        self.tree = frequent_pattern_tree
        self.frequent_items = frequent_pattern_tree.frequentItems
        self.min_supp = min_support

    def build_frequent_closed_itemset(self):
        if self.tree is None:
            return []

        fci = []
        self.closet_algorithm([], self.tree, self.frequent_items, fci)
        return fci

    def closet_algorithm(self, candidate_frequent_itemset, tdb, f_list, fci):
        items_in_every_transaction = f_list.get_items_in_every_transaction(tdb)
        f_list.erase(items_in_every_transaction)

        candidate_frequent_itemset.add(items_in_every_transaction)
        fci.try_add(candidate_frequent_itemset)

        tree = self.create_tree(f_list, tdb)

        f_list.sort_ascending()
        for item in f_list.items:
            subset_tdb = tree.get_transactions_associated_with(item)
            frequent_itemset = candidate_frequent_itemset.add(item)
            subset_f_list = FrequentItemSet(subset_tdb)
            self.closet_algorithm(frequent_itemset, subset_tdb, subset_f_list, fci)

