from collections import Counter


class Inventory(object):
    """docstring for Inventory"""
    def __init__(self, capacity):
        super(Inventory, self).__init__()
        self.capacity = capacity
        # self.items = []
        self.stackable_items = {}
        self.unstackable_items = []

    @property
    def items(self):
        result = []
        for (_, (item, count)) in self.stackable_items.items():
            result.append((item, count))
        for item in self.unstackable_items:
            result.append((item, 1))
        return result

    # @items.setter
    # def items(self, items):
        # self.__items = items

    def add_item(self, item):
        results = []

        # if len(self.items) >= self.capacity:
            # results.append({
                # 'item_added': None,
                # 'msg': "Inventory is Full."
            # })
        # else:
        results.append({
            'item_added': item,
            'msg': "pickedup " + str(item.name)
        })

        if item.item.stackable:
            if self.stackable_items.get(item.name):
                _, count = self.stackable_items[item.name]
                self.stackable_items[item.name] = (item, count+1)
            else:
                self.stackable_items[item.name] = (item, 1)
        else:
            self.unstackable_items.append(item)
        return results

    def remove_item(self, item_entity):
        if item_entity.item.stackable:
            item, count = self.stackable_items[item_entity.name]
            self.stackable_items[item_entity.name] = (item, count-1)
            if count - 1 == 0:
                del self.stackable_items[item_entity.name]
        else:
            self.__items.remove(item_entity)

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

    # def item_quantity(self, item):
        # return self.items[item]
