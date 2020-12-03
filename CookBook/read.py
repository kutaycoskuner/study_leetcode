def Main(): 
    f = open("../database/sometext.txt","r") # :: r for read
    for line in f:
        print(line)
    f.close()

if __name__ == "__main__":
    Main()