from project.product import Product


class Beverage(Product):
    def __init__(self,name, price, mililiters):
        Product.__init__(self, name, price)
        self._mililiters = mililiters

    @property
    def mililiters(self):
        return self.mililiters

