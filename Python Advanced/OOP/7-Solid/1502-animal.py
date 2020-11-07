# # Решение на задачата по питонски :)
# sounds_mapper = {"cat": "meow", "dog": "woof-woof", "chicken": "chick"}
#
#
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         try:
#             print(sounds_mapper[animal.species.lower()])
#         except:
#             print("Unknown")
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)

# по-обширно решение

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, ):
        self.sound = "meow"

    def make_sound(self):
        return self.sound


class Dog(Animal):
    def __init__(self):
        self.sound = 'bark bark'

    def make_sound(self):
        return self.sound + "showing teeth"


animals = [Dog() , Cat()]
for a in animals:
    print(a.make_sound())
