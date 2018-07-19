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

    def remove_item(self, item_entity):
        self.items.remove(item_entity)

    def use_item(self, item_entity, **kwargs):
        results = []

        item = item_entity.item

        if item.use_function is None:
            pass
        else:
            kwargs = {**item.function_kwargs, **kwargs}
            use_results = item.use_function(self.owner, **kwargs)

            for use_result in use_results:
                if use_result.get('item_used'):
                    self.remove_item(item_entity)

            results.extend(use_results)

        return results
