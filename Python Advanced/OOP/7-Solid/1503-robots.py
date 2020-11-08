from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def senzors_count(self):

class Android(Robot):
    def senzors_count(self):
        return 4


class Chappie(Robot):
    def senzors_count(self):
        return 6



robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)
