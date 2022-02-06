#
# ==== Roman to Integer
def Main():
    # ==== test
    s = "III"
    
    # ==== logic
    # :: get last two character
    isExists4 = s.find("IV")
    isExists9 = s.find("IX")
    isExists40 = s.find("XL")
    isExists90 = s.find("XC")
    isExists400 = s.find("CD")
    isExists900 = s.find("CM")

    # :: initial value
    splitRoman = list(s)
    number = 0
    number += splitRoman.count('I') * 1
    number += splitRoman.count('V') * 5
    number += splitRoman.count('X') * 10
    number += splitRoman.count('L') * 50
    number += splitRoman.count('C') * 100
    number += splitRoman.count('D') * 500
    number += splitRoman.count('M') * 1000
    
    # :: reduce the number
    if isExists4 != -1:
        number -= 2
    if isExists9 != -1:
        number -= 2
    if isExists40 != -1:
        number -= 20
    if isExists90 != -1:
        number -= 20
    if isExists400 != -1:
        number -= 200
    if isExists900 != -1:
        number -= 200

    # :: 
    print(number)
    return number

if __name__ == "__main__":
    Main()