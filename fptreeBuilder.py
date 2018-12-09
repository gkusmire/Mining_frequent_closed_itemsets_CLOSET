import csv

from Mining_frequent_closed_itemsets_CLOSET.fpTree.fpTree import FPTree
from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItemset import FrequentItemSet
from Mining_frequent_closed_itemsets_CLOSET.itemDictionary import ItemDictionary


class FPTreeBuilder:
    def __init__(self, file_name, min_support):
        self.file_name = file_name
        self.min_support = min_support
        self.dictionary = ItemDictionary()

    def get_fptree(self):
        frequent_items = self.get_frequent_itemset()
        frequent_items.sort_descending()
        return self.build_fptree(frequent_items)

    def get_frequent_itemset(self):
        itemset = FrequentItemSet()

        with open(self.file_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            transaction_counter = 0
            for row in reader:
                if transaction_counter == 0:
                    transaction_counter += 1
                else:
                    for item in row:
                        itemset.add(self.dictionary.get_id(item))
                        transaction_counter += 1
        itemset.remove_not_frequent_items(self.min_support)
        return itemset

    def build_fptree(self, frequent_itemset):
        fptree = FPTree(frequent_itemset)

        with open(self.file_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            first_line = True
            for row in reader:
                if first_line is True:
                    first_line = False
                else:
                    items_id = []
                    for x in row:
                        items_id.append(self.dictionary.get_id(x))
                    fptree.add_itemset(items_id)
        fptree.extract_items_associated_in_every_transaction()
        return fptree
