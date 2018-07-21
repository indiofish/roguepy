class Item(object):
    def __init__(self, use_function=None, stackable=True, **kwargs):
        self.use_function = use_function
        self.stackable = stackable
        self.function_kwargs = kwargs
