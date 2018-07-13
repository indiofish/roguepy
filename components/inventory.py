class Inventory(object):
    """docstring for Inventory"""
    def __init__(self, capacity):
        super(Inventory, self).__init__()
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'msg': "Inventory is Full."
            })
        else:
            results.append({
                'item_added': item,
                'msg': "pickedup " + str(item.name)
            })
            self.items.append(item)
        return results
