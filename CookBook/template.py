from string import Template

class MyTemplate(Template):
    delimiter = "#"

def Main():
    cart = []
    cart.append(dict(item="ball", price=32, qty=2))
    cart.append(dict(item="cake", price=8, qty=1))
    cart.append(dict(item="fish", price=16, qty=4))

    t = MyTemplate("#qty x #item = #price")
    total = 0
    print("Cart: ")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]

    print("Total: " + str(total))

if __name__ == "__main__":
    Main()