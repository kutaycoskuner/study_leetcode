def greet_user():
    """ Generic greeting for users """
    print("hello")
    print("Welcome")

def greet_user_by_name(name="user", greeting="hello"):
    """ Customized Greeting """
    print(greeting + name)

def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value


greet_user()
greet_user_by_name(input("what is your name? "), "Welcome ")
greet_user_by_name()
greet_user_by_name("Orthrin", "Welcome ")
greet_user_by_name(greeting="welcome ", name="orthrin")

eleven_cubed = cube(11)
print(eleven_cubed)
