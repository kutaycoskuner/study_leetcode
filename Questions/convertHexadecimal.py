#
# ==== Convert a Number to Hexadecimal
# :: Template 1.5
# :: leetcode: 405
# :: https://leetcode.com/problems/convert-a-number-to-hexadecimal/

# == Procedure
# :: - template edit if any
# :: - change title
# :: - change leetcode number
# :: - link of the question
# :: - rename function
# :: - create test cases and test

# == Complexity Analysis
# :: M ..

# == Notes
# :: 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
# :: 26 = 16 + 10 1a
# :: 10     -> 5 | :2 | k0                              == 20
# :: 20     -> 5 | :4 | k0                              == 40
# :: 50     -> 5 | :10 | k0  -> :2 | k0                 == 200  
# :: 61     -> 5 | :12 | k1  -> :2 | k2                 == 221
# :: 100    -> 5 | :20 | k0  -> :4 | k0                 == 400
# :: 106    -> 5 | :21 | k1  -> :4 | k1                 == 411
# ::                     ^3     ^1   ^2
# :: [Son bolum + son kalan] + sirayla onceki kalanlar


# == Functions
def solution(num):
    # :: solve negative
    if num < 0:
        num += 2**32
    
    # :: Taban cevirici
    new = []
    taban = 16
    loop = True
    while loop:
        kalan1 = num % taban;
        bolum1 = (num - kalan1) // taban   
        # :: tabandan buyuk ise ustteki islemi bir daha uygula
        if bolum1 >= taban:
            loop = True
            new.insert(0, kalan1)
            num = bolum1
        else: 
            loop = False
            new.insert(0, kalan1)
            if bolum1 != 0:
                new.insert(0, bolum1)        
    
    # :: dictinoary
    hexadecimal = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
        10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"
    }
    
    # :: kalanlari a b c diye ayir
    ans = ""
    for ii in range(0, len(new)):
        ans += hexadecimal[new[ii]]

    return ans

def Main():
    # ==== test cases
    testsolo = 5
    test = [
        4, 5, 25, 61, 106, -1, -16
    ]

    # ==== test py 
    for ii in range(len(test)):
        print(str(test[ii]) + " " + str(solution((test[ii]))))

# ==== Main
if __name__ == "__main__":
    Main()


