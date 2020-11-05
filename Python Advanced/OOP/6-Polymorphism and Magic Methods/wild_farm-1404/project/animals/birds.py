from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return f"Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.25* food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += 0.35* food.quantity
        self.food_eaten += food.quantity
        return
