class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # :: you can run super class methods as this

def Main():
    thePet = Pet("Pet", 1)
    kedi = Cat("Kedi", 1)

    print("is kedi a pet? " + str(isinstance(kedi, Pet)))
    print("is kedi a cat? " + str(isinstance(kedi, Cat)))
    print("is thePet a pet? " + str(isinstance(thePet, Pet)))
    print("is thePet a cat? " + str(isinstance(thePet, Cat)))

if __name__ == "__main__":
    Main()