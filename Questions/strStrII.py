#
# ==== Implement Strstr()
# . Template 2.2
# . leetcode: 28
# . level : easy
# . https://leetcode.com/problems/implement-strstr/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - create test cases and test

# == Complexity Analysis
# Time complexity
# Space Complexity

# == Notes

# == Classes

# == Functions

# == Libraries

# == Solution
def solution(haystack, needle):
        ii = 0              #:: iterator
        isMatch = True      #:: tam eslesme var mi yok mu?
        isFailSet = False   #:: match kontrolunun fail olmasi durumunda baslangic noktasi ayarlandi mi
        failStartPoint = 0  #:: eslesme bulamazsa geri donup baslayacagi nokta
        # :: hay loopa basla
        while ii < len(haystack):
            # :: ilk karakterle karsilasma bul
            if haystack[ii] == needle[0]:
                isMatch = True
                isFailSet = False
                failStartPoint = 0
                # :: haystack in geri kalaninda needle kadar uzunluk var mi diye kontrol et
                if len(haystack) - ii >= len(needle):
                    # :: geri kalan karakterleri karsilastir
                    for yy in range(1, len(needle)):
                        # :: ilk karakterle yeniden karsilastim mi?
                        if haystack[ii+yy] == needle[0]:
                            isFailSet = True
                        if not isFailSet:
                            failStartPoint += 1
                        if haystack[ii+yy] != needle[yy]:
                            isMatch = False
                            break
                    # :: full eslesme var ise return
                    if isMatch:
                        return ii
                    else:
                        ii += failStartPoint
            ii += 1
        return -1

def Main():
    # ==== test solo
    # :: variables
    # input = 'hello'
    # input2 = 'll'
    # expected = 2

    # print("solution: ", solution(input,input2), " expected: ", expected)
    # return 0
    # :: display

    # ==== test batch
    input1 = [
        "hello",
        "aaaaa",
        "kutai kutai kutai kutay",
        "missisisssipississipsipipisisipis",
        "aaaa"
        #012345678901234567890123
    ]

    input2 = [
        "ll",
        "bba",
        "kutay",
        "issip",
        "aaa"
    ]

    output1 = [
        2,
        -1,
        18,
        15,
        0
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii], input2[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
