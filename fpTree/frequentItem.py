class FrequentItem:
    def __init__(self, name_):
        self.name = name_
        self.frequent_counter = 0
        self.node_link = None
        self.last_added_node = None

    def increment_counter(self):
        self.frequent_counter += 1
