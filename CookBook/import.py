import math

def Main():
    try:
        number = float(input("Please input a number: "))
        number = math.fabs(number) # :: absolute
        print(number)
    except:
        print('you did not enter a number')

if __name__ == "__main__":
    Main()