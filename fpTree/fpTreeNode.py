class Node:
    def __init__(self, item_):
        self.item = item_
        self.node_link = None
        self.counter = 0
        self.parent_link = None
        self.childrenNodes = []

    def increment_counter(self):
        self.counter += 1

    def add_children(self, node):
        self.childrenNodes.append(node)

    def get_children(self, item_element):
        for child in self.childrenNodes:
            if child.item is item_element:
                return child
        return None
