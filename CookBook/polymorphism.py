class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # :: you can run super class methods as this

    def talk(self):
        return "meow"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # :: you can run super class methods as this

    def talk(self):
        return "woof"



def Main():

    pets = [Cat('jess', 3), Dog('jack', 2), Cat('cos', 6), Pet('tunc', 3)]

    for pet in pets:
        print("Name: " + pet.name + ", Age: " + str(pet.age) + ", says " + pet.talk())

if __name__ == "__main__":
    Main()