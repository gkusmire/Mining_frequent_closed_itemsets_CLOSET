
class ItemDictionary:
    def __init__(self):
        self.dictionary = dict()
        self.id = 0

    def get_id(self, item_name):
        for x in range(self.id):
            if self.dictionary[x] == item_name:
                return x
        self.dictionary[self.id] = item_name
        self.id += 1
        return self.id - 1
