#
# ==== Last Stone Weight
# . Template 2.2
# . leetcode: 1046
# . level : easy
# . https://leetcode.com/problems/last-stone-weight/

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
def solution(stones):
    while len(stones) > 1:
        stones.sort(reverse=True)
        stones[0] = stones[0] - stones[1]
        if stones[0] == 0 and len(stones) > 2:
            del stones[:2]
        else:
            del stones[1]
    return stones[0]


def Main():
    # ==== test solo
    # :: variables
    # input = [2, 7, 4, 1, 8, 1]
    # expected = 1

    # print("solution: ", solution(input), " expected: ", expected)
    # return 0
    # :: display

    # ==== test batch
    input1 = [
        [2, 7, 4, 1, 8, 1],
        [1],
        [1,3],
        [2,2]
        # 012345678901234567890123
    ]

    output1 = [
        1,
        1,
        2,
        0
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii])) + " Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
