class Hero:
    def __init__(self, name: str, health: float):
        self.name = name
        self.health = health

    def defend(self, damage: float):
        if self.health - damage <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        self.health -= damage

    def heal(self, amount: float):
        self.health += amount
