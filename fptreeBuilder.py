import csv

from Mining_frequent_closed_itemsets_CLOSET.fpTree.fpTree import FPTree
from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItemset import FrequentItemSet


class FPTreeBuilder:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_fptree(self):
        frequent_items = self.get_frequent_itemset()
        frequent_items.sort_descending()
        return self.build_fptree(frequent_items)

    def get_frequent_itemset(self):
        itemset = FrequentItemSet()

        with open(self.file_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            first_line = True
            for row in reader:
                if first_line is True:
                    first_line = False
                else:
                    for item in row:
                        itemset.add(item)

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
                    fptree.add_itemset(row)
        return fptree
