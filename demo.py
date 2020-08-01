class defaultdict:
    def __init__(self, factory_fn):
        self.__factory_fn = factory_fn
        self.__dict = {}

    def __getitem__(self, item):
        if item not in self.__dict:
            self.__dict[item] = self.__factory_fn()
        return self.__dict[item]