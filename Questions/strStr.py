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
def solution(hay, needle):
    # :: hay loopa basla
    for ii in range (len(hay)):
        # :: ilk karakterle karsilasma bul
        if hay[ii:ii+len(needle)] == needle:
            return ii
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
        "missisisssipississipsipipisisipis"
        #012345678901234567890123
    ]

    input2 = [
        "ll",
        "bba",
        "kutay",
        "issip"
    ]

    output1 = [
        2,
        -1,
        18,
        15
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii], input2[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
