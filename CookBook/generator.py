def Reverse(data):
    for index in range(len(data)-1, -1, -1): #:: start, end, iteration
        yield data[index]

def Main():
    rev = Reverse("Kutay")
    for char in rev:
        print(char)

    data = "Kutay"
    print(list(data[i] for i in range(len(data)-1, -1, -1)))

if __name__ == "__main__":
    Main()