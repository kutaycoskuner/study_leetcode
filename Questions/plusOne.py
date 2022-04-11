#
# ==== Plus One
# . Template 2.3
# . leetcode: 66
# . level : easy
# . https://leetcode.com/problems/plus-one/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - create test cases and test

# == Complexity Analysis
# Time complexity       log n   | prev: n log n
# Space Complexity

# == Notes
# . Solution 1
#       . arrayi birlestirip sayi yap
#       . bir ekle
#       . sayiyi ayirip array yap

# . Solution 2
# . for: geriden iterasyon
# .     if: karakter 9 dan kucuk ise bir arttir kir
# .     else: karakteri sifira esitle
# . if: butun islem bitince array boyunu uzatmak gerekiyorsa uzat

# == Libraries

# == Classes

# == Functions

# == Solution
def solution(digits):
    extend = True
    for ii in reversed(range(len(digits))):
        if digits[ii] < 9:
            extend = False
            digits[ii] += 1
            break
        else: 
            digits[ii] = 0
    if extend:
        digits.insert(0,1)
    return digits

    # :: hack solution
    # num = ""
    # arr = []
    # for ii in digits:
    #     num = str(num) + str(ii)
    # num = int(num) + 1
    # for ii in str(num):
    #     arr.append(int(ii))
    # return arr

def Main():
    # ==== test solo
    # # :: variables
    # input = [1,2,3]  # stre
    # expected = [1,2,4]

    # print("solution: ", solution(input), " expected: ", expected)
    # return 0

    # ==== test batch
    input1 = [
        [1,2,3],
        [4,3,2,1],
        [9]
        # 012345678901234567890123
    ]

    output1 = [
        [1,2,4],
        [4,3,2,2],
        [1,0]
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
