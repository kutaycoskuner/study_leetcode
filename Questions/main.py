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
    match = True
    # :: hay loopa basla
    ii = 0
    while ii < len(hay):
        # :: ilk karakterle karsilasma bul
        if hay[ii] == needle[0]:

            # :: match resetle
            match = True
            # :: sonrkaileri karsilastir
            for jj in range(0, len(needle)):
                # print(needle[jj], " ", hay[jj + ii])
                # :: n. karakter tutmuyor ise
                if needle[jj] != hay[ii + jj]:
                    ii += jj
                    match = False
                    break

            # :: return
            if match:
                return ii
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
        "missisisssipississipsipi"
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
        10
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii], input2[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
