#
# ==== Polymorphism
# == Super Class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

# == Sub Classes
class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # :: you can run super class methods as this

    def talk(self):
        return "woof"

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # :: you can run super class methods as this

    def talk(self):
        return "meow"