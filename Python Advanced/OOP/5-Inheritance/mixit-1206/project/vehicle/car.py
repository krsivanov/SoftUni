# from project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        # super().__init__(available_seats)
        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value + self.__fuel <= self.fuel_tank:
            self.__fuel = value

    def drive(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if fuel_needed <= self.__fuel:
            self.__fuel -= fuel_needed
            return f"We've enjoyed the travel!"

    def refuel(self, liters):
        try:
            self.get_capacity(self.fuel_tank, self.fuel + liters)
            self.__fuel += liters
            return self.__fuel
        except Exception as ex:
            return str(ex)
#
#
# car = Car(4, 50, 3, 50)
# print(car.drive(5))
# print(car.fuel)
# print(car.refuel(13))
# print(f"car fuel is {car.fuel}")
