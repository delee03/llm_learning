class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        return "Meow"

class Dog(Animal):
    def sound(self):
        return "Woof"
class Monkey(Animal):
    def sound(self):
        return "Hoo Hoo"


animals = [Cat(), Dog(), Monkey()]
for animal in animals:
    print(animal.sound())

