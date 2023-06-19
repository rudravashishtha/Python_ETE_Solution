# Question 35
class Animal:
    def __init__(self, name="This Animal"):
        self.name = name
    def eat(self, food="Grass"):
        print(self.name, "eats", food)
class Mammal(Animal):
    def eat(self):
        print(self.name, "does not eat. It only drinks")
class WingedAnimal(Animal):
    def eat(self):
        print(self.name, "eats anything and everything")
class Bat(WingedAnimal, Mammal):
    def smell(self):
        print("This Animal Stinks")
class FruitBat(Mammal, WingedAnimal):
    pass

rabbit1 = Animal("Rabbit")
print("Rabbit1 is an instance of Animal")
rabbit1.eat()
rabbit1.eat("Peanuts")

print("Cow1 is an instance of Mammal")
cow1 = Mammal("Cow")
cow1.eat()

print("Vulture1 is an instance of WingedAnimal")
vulture1 = WingedAnimal("Vulture")
vulture1.eat()

print("Bat1 is an instance of Bat")
bat1 = Bat("Bat")
bat1.eat()

print("fbat is an instance of FruitBat")
fbat = FruitBat("Fruitbat")
fbat.eat()
