from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILILITERS = 50
    COFFEE_PRICE = 3.50
    def __init__(self, name, caffeine):
        HotBeverage.__init__(self, name, Coffee.COFFEE_PRICE,Coffee.COFFEE_MILILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
