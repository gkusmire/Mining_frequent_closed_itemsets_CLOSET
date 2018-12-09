class FrequentItemsetItem:
    def __init__(self, itemset=None, frequency=0):
        if itemset is None:
            itemset = []
        self.frequency = frequency
        self.itemset = itemset

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_itemset(self, itemset):
        self.itemset = itemset

    def add(self, element, element_frequency):
        if element_frequency < self.frequency:
            self.frequency = element_frequency
        self.itemset.append(element)

    def is_subset(self, item):
        if self.frequency > item.frequency:
            return False
        for x in self.itemset:
            if not(x in item.itemset):
                return False
        return True

    def is_superset(self, item):
        if self.frequency < item.frequency:
            return False
        for x in item.itemset:
            if not(x in self.itemset):
                return False
        return True

    def copy_values(self, item):
        self.frequency = item.frequency
        for x in item.itemset:
            self.itemset.append(x)


class FrequentClosedItemset:
    def __init__(self):
        self.items = []

    def try_add(self, candidate_itemset):
        for x in self.items:
            if x.is_subset(candidate_itemset):
                x = candidate_itemset
                return True
            if x.is_superset(candidate_itemset):
                return False
        self.items.append(candidate_itemset)
        return True
