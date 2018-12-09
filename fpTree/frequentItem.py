class FrequentItem:
    def __init__(self, name_, frequency=1):
        self.name = name_
        self.frequent_counter = frequency
        self.node_link = None
        self.last_added_node = None

    def increment_counter(self, frequency=1):
        self.frequent_counter += frequency
