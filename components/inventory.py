class Inventory(object):
    """docstring for Inventory"""
    def __init__(self, capacity):
        super(Inventory, self).__init__()
        self.capacity = capacity
        self.items = []
