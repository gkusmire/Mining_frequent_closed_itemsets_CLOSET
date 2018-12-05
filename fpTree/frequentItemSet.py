from Mining_frequent_closed_itemsets_CLOSET.fpTree.item import Item


class FrequentItemSet:

    def __init__(self):
        self.items = []

    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                return item

        item = Item(name)
        self.items.append(item)
        return item

    def sort_descending(self):
        self.items.sort(key=lambda item: item.counter, reverse=True)
