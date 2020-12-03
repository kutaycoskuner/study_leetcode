def Main(): 
    words = ["cat","bat","math"]
    with open("../database/sometext.txt","w") as file: # :: r for read
        for ii in range(2):
            file.write(input("Please enter a word: ") + "\n")

if __name__ == "__main__":
    Main()