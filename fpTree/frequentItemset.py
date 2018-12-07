from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItem import FrequentItem


class FrequentItemSet:

    def __init__(self):
        self.items = []

    def get(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def add(self, name):
        self.items.append(FrequentItem(name))

    def sort_descending(self):
        self.items.sort(key=lambda item: item.frequent_counter, reverse=True)

    def register_item(self, name):
        if self.get(name) is None:
            self.add(name)
        else:
            self.get(name).increment_counter()
