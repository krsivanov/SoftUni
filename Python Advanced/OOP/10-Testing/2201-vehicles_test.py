from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + 0.9):
            self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + 1.6):
            self.fuel_quantity -= distance * (self.fuel_consumption + 1.6)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95



import unittest
class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(100, 2)


    def test_drive_notEnough_fuel(self):

        self.car.drive(40)

        self.assertEqual(self.car.fuel_quantity, 100)

    def test_drive_car_enough_fuel(self):

        self.car.drive(10)

        self.assertEqual(self.car.fuel_quantity, 71)

    def test_refuel(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_quantity, 150)

class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100,6)

    def test_driveTruck_notEnough_fuel(self):

        self.truck.drive(40)

        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_drive_truck_enough_fuel(self):

        self.truck.drive(10)

        self.assertEqual(self.truck.fuel_quantity, 24)

    def test_refuel(self):
        self.truck.refuel(50)
        self.assertEqual(self.truck.fuel_quantity, 147.5)


if __name__ == "__main__":
    unittest.main()
