class MyClass:
    number = 0
    name = "potato"

def Main():
    me = MyClass()
    me.number = 29
    me.name = "Kutay"

    friend = MyClass()
    friend.number = 3
    friend.name = "S"

    print('Name: ' + me.name + ", favourite number: " + str(me.number)) 
    print('Name: ' + friend.name + ", favourite number: " + str(friend.number))

if __name__ == "__main__":
    Main()