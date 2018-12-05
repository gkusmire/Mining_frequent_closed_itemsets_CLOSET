class Node:

    def __init__(self, name_, node_link_):
        self.name = name_
        self.node_link = node_link_
        self.counter = 0
        self.childrenNodes = []

    def incrementCounter(self):
        self.counter += 1

    def addChildren(self, node):
        self.childrenNodes.append(node)