#
# ==== Search a 2D Matrix 2
# . Template 2.7
# . Start Date 07-May-2022
# . leetcode: 74
# . level : medium
# . https://leetcode.com/problems/search-a-2d-matrix/

# == Result
# . time:   58
# . memory: 90

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
# . a b c d e
# . f g h i i
# . [j] k l m [n]
# . p r s s t

# . 1 2 3
# . 4 5 6
# . 7 8 9

# . 1 2 3 4
# . 5 6 7 8

# == Libraries
import sys

# == Classes

# == Functions
def binarySearch(arr, tar):
    start = 0
    end = len(arr) - 1 
    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == tar:
            return True
        if arr[mid] < tar:
            start = mid + 1
        else:
            end = mid - 1
    return False

# == Solution
def solution(matrix, target):
    rowSize = len(matrix)
    colSize = len(matrix[0])
    start = 0
    end = rowSize * colSize - 1
    while start <= end:
        mid = (end + start) // 2
        # :: col/row hesapla
        col = mid % colSize 
        row = mid // colSize 
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

def solution1(matrix, target):
    # :: parameters
    start = 0
    end = len(matrix)-1
    # :: loop
    while start <= end:
        # :: dynamic vars
        mid = (end + start) // 2
        # print(start, end, mid)
        lenRow = len(matrix[mid])    
        # :: check if equal
        if matrix[mid][lenRow-1] == target:
            return True
        # :: check if smaller
        if matrix[mid][lenRow-1] < target:
            start = mid + 1
        if matrix[mid][lenRow-1] > target:
            # :: if current
            if matrix[mid][0] == target:
                return True
            # :: if same row
            if matrix[mid][0] < target:
                return binarySearch(matrix[mid], target)
            # :: if not in same row    
            end = mid - 1
    return False

def Main():
    # ==== test batch
    input1 = [
    [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]],
    [[1],[3]],
    [[1]],
    [[1,1]],
    [[1]],
    [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
    [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
    [[1],[3],[5]]
    ]

    input2 = [
        -5,
        3,
        1,
        2,
        2,
        3,
        13,
        5
    ]

    output1 = [
        True,
        True,
        True,
        False,
        False,
        True,
        False,
        True
    ]

    # :: 
    # arr = [1,2,3,4,5,6,7,8]
    # tar = 8
    # print(binarySearch(arr,tar))
    # return
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
