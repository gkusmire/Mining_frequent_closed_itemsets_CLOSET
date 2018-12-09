from Mining_frequent_closed_itemsets_CLOSET.fpTree.frequentItem import FrequentItem


class FrequentItemSet:

    def __init__(self):
        self.items = []

    def get(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def add(self, name, frequency=1):
        item = self.get(name)
        if item is None:
            self.items.append(FrequentItem(name, frequency))
        else:
            item.increment_counter(frequency)

    def sort_descending(self):
        self.items.sort(key=lambda item: item.frequent_counter, reverse=True)

    def sort_ascending(self):
        self.items.sort(key=lambda item: item.frequent_counter, reverse=False)

    def register_item(self, name):
        if self.get(name) is None:
            self.add(name)
        else:
            self.get(name).increment_counter()

    def remove_not_frequent_items(self, min_supp):
        for element in self.items:
            if element.frequent_counter < min_supp:
                self.items.remove(element)

    def delete(self, item):
        for element in self.items:
            if element.name == item.name:
                self.items.remove(element)
