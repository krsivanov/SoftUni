class Animal:
    def eat(self):
        return 'eating...'

class Dog(Animal):
    def bark(self):
        return 'baring...'


d = Dog()

print(d.eat())
print(d.bark())