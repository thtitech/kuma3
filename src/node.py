class Node:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other
    def __ne__(self, other):
        return self.name != other
