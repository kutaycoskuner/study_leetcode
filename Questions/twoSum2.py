#
# ==== Two Sum
# . Template 2.5
# . Start Date 14-Apr-2022
# . leetcode: 1
# . level : easy
# . https://leetcode.com/problems/two-sum/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - create test cases and test

# == Complexity Analysis
# . Time complexity       log n   | prev: n log n
# . Space Complexity

# . optimal cozumu goremiyorsan brute force
# . complexity analysis | time ve space
# . gorsellestir redundant work ara | veri yapisi | adim
# . redundancy yi kod uzerinde tespit et (pattern recognition)
# . cozum ara

# == Notes
# . dictionary [index, value]
# . 2, 11, 15, 7
# . ^
# . 9 - 2 dictonaryde ise return 
# . yoksa dictionary ye ekle
# . 2, 11, 15, 7
# .     ^
# . lf= -2 dict = [2]
# . 2, 11, 15, 7
# .         ^    
# . lf= -6 dict = [2, 11]
# . 2, 11, 15, 7
# .            ^    
# . lf= 2 [2, 11, 15]

# == Libraries

# == Classes

# == Functions

# == Solution
def solution(nums, expected):
    dict = {}
    for ii in range(len(nums)):
        lf = expected - nums[ii]
        # :: kontrol if rturn
        if lf in dict:
            return [dict[lf], ii]
        # :: ekle
        dict[nums[ii]] = ii

def Main():
    # ==== test solo
    # :: variables
    input = [2,7,11,15]
    expected = 9
    output = [0,1]

    # print("solution: ", solution(input, expected), "\t\t expected: ", output)
    # return 0

    # ==== test batch
    input1 = [
        [2,7,11,15],
        [3,2,4],
        [3,3]
    ]
    input2 = [
        9,
        6,
        6
    ]

    output1 = [
        [0,1],
        [1,2],
        [0,1]
    ]

    # :: test batch
    for ii in range(len(output1)):  # len(test1)
        print("Test " + str(ii+1) + " Output: " +
              str(solution(input1[ii], input2[ii])) + "\t\t Expected: " + str(output1[ii]))


# ==== Main
if __name__ == "__main__":
    Main()
