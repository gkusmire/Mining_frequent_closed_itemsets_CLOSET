class FrequentItemsetItem:
    def __init__(self, itemset=None, frequency=None):
        if itemset is None:
            itemset = []
        self.frequency = frequency
        self.itemset = itemset

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_itemset(self, itemset):
        self.itemset = itemset

    def add(self, element, element_frequency):
        if self.frequency is None:
            self.frequency = element_frequency
        else:
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

    def print(self, d):
        for x in self.itemset:
            print(d.dictionary[x], end=' ')
        print("FREQUENCY: ", end=" ")
        print(self.frequency)
        print("")


class FrequentClosedItemset:
    def __init__(self, min_support):
        self.items = []
        self.min_support = min_support

    def try_add(self, candidate_itemset):
        if candidate_itemset.frequency is None:
            return False
        if candidate_itemset.frequency < self.min_support:
            return False
        if len(candidate_itemset.itemset) < 1:
            return False
        for x in self.items:
            if x.is_subset(candidate_itemset):
                x = candidate_itemset
                print("AAA")
                return True
            if x.is_superset(candidate_itemset):
                print("BBB")
                return False
        self.items.append(candidate_itemset)
        return True

    def print(self, d):
        print("Zbiór zamknięty")
        for x in self.items:
            x.print(d)
        print("Koniec zbioru")
