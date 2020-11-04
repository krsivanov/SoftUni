from project.parking_mall.parking_mall import ParkingMall


class Level1(ParkingMall):
    def __init__(self):
        ParkingMall.__init__(self, 150)

#
# l_1 = Level1()
# print(l_1.check_availability())
