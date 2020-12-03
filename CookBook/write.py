def Main(): 
    f = open("../database/sometext.txt","w") # :: r for read
    for ii in range(2):
        f.write(input("Please enter a word: ") + "\n")
    f.close()

if __name__ == "__main__":
    Main()