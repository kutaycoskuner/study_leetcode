#
# ==== Contains Duplicate 
# . Template 2.3
# . leetcode: 217
# . level : easy
# . https://leetcode.com/problems/contains-duplicate/

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
# . var -> unique kontrolu icin set olustur
# . for: array ustunde iterasyon
# .     if: sette karsiligi yoksa ekle
# .     else: break    

# == Libraries

# == Classes

# == Functions

# == Solution
def solution(nums):
    uniqueSet = set(nums)
    return len(nums) != len(uniqueSet)
    



def Main():
    # ==== test solo
    # :: variables
    # input = [1,2,3,1]  # stre
    # expected = True

    # print("solution: ", solution(input), " expected: ", expected)
    # return 0

    # ==== test batch
    input1 = [
        [1,2,3,1],
        [1,2,3,4],
        [1,1,1,3,3,4,3,2,4,2]
        # 012345678901234567890123
    ]

    output1 = [
        True,
        False,
        True
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
