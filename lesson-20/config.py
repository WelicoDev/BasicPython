from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def color(self):
        pass

class Dog(Animal):
    def speak(self):
        print("woof-woof")

    def color(self):
        print("black")

class Cat(Animal):
    def speak(self):
        print("meow-meow")

class Horse(Animal):
    def speak(self):
        print("Woof-woof")


d = Dog()
c = Cat()
h = Horse()

d.speak()
c.speak()
h.speak()