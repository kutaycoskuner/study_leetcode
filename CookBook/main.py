def getInteger():
    result = int(input("Please enter an integer: "))
    return result

def Main(): 
    print('program started')
    output = getInteger()
    print(output)

if __name__ == "__main__":
    Main()