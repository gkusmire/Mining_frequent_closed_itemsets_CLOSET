class Item:

    def __init__(self, name):
        self.name = name
        self.counter = 0
        self.pointer = 0

    def increment_counter(self):
        self.counter += 1
