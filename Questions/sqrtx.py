#
# ==== Sqrt(x)

# == Procedure
# 1. change title
# 2. rename function
# 3. create test cases and test

# == Complexity Analysisis
# M : liste boyutu
# N : longest string length

# == Functions
def sqrt(x):
    if x == 1 or x == 2:
        return 1
    output = 0
    for ii in range(0, x):
        square = ii**2
        if square == x:
            output = ii
            break
        if square > x:
            output = ii-1
            break
    return output


def Main():
    # ==== test cases
    x = 4            # :: 2       
    x1 = 8           # :: 2  | 2.8-
    x2 = 16          # :: 4
    x3 = 169         # :: 13
    x4 = 225         # :: 15
    x5 = 0           # :: 0
    x6 = 1           # :: 1
    x7 = 2           # :: 1

    # ==== testpy 
    print(sqrt(x))
    print(sqrt(x1))
    print(sqrt(x2))
    print(sqrt(x3))
    print(sqrt(x4))
    print(sqrt(x5))
    print(sqrt(x6))
    print(sqrt(x7))

# ==== Main
if __name__ == "__main__":
    Main()


