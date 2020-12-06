from abc import ABC, abstractmethod


class Supply:
    @abstractmethod
    def __init__(self, needs_increase):
        self.needs_increase = needs_increase

    @property
    def needs_increase(self):
        return self._needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self._needs_increase = value

    def apply(self, survivor):
        survivor.need += self.needs_increase
