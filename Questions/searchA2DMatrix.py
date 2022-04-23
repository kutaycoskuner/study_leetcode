#
# ==== Search a 2D Matrix
# . Template 2.7
# . Start Date 23-Apr-2022
# . leetcode: 74
# . level : medium
# . https://leetcode.com/problems/search-a-2d-matrix/

# == Result
# . time:   92.33
# . memory: 21.55

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
#. her row un son karakterine bak
#. son karakteri buyukse veya esitse ilk karaktere bak
#. loop

# == Libraries
import sys

# == Classes

# == Functions

# == Solution
def solution(matrix, target):
    for ii in range(len(matrix)):
        if target <= matrix[ii][len(matrix[ii])-1]:
            if matrix[ii][len(matrix[ii])-1] == target:
                return True
            else: 
                for jj in matrix[ii]:
                    if jj == target:
                        return True
                return False

def Main():
    # ==== test batch
    input1 = [
    [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
    [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    ]

    input2 = [
        3,
        13
    ]

    output1 = [
        True,
        False
    ]

    # :: argument identification
    if len(sys.argv) >= 2:
        args = int(sys.argv[1])
    else:
        args = None
    # :: test batch
    if args == None:
        for ii in range(len(output1)):  # len(test1)
            print("Test " + str(ii+1) + " Output: " +
                str(solution(input1[ii], input2[ii])) + "\t Expected: " + str(output1[ii]))
            # print(str((solution(input1[ii]) == output1[ii])))
    else:
        answer = solution(input1[args-1])
        print("Test " + str(args) + " Output: " +
                str(answer) + "\t Expected: " + str(output1[args-1]) + '\n' + str(answer == output1[args-1]))


# ==== Main
if __name__ == "__main__":
    Main()
