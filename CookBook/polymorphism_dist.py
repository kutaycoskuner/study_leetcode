from Modules.Pet import *

def Main():

    pets = [Cat('jess', 3), Dog('jack', 2), Cat('cos', 6)]

    for pet in pets:
        print("Name: " + pet.name + ", Age: " + str(pet.age) + ", says " + pet.talk())

if __name__ == "__main__":
    Main()