import math
from abc import ABC, abstractmethod



class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height


class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def calculate_area(self):
        return (self.side * self.h) / 2

class Circle(Shape):
    def __init__(self,r):
        self.radius = r

    def calculate_area(self):
        return (math.pi*self.radius*self.radius)


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Triangle(1, 6),Circle(5)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
