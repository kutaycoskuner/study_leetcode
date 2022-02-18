#
# ==== Matrix Diagonal Sum
# :: Template 1.6
# :: leetcode: 1572
# :: https://leetcode.com/problems/matrix-diagonal-sum/

# == Procedure
# :: - template edit if any
# :: - change title
# :: - change leetcode number
# :: - link of the question
# :: - create test cases and test

# == Complexity Analysis
# :: M ..

# == Notes
# ::

# == Functions
def solution(mat):
    sum = 0
    # :: 1. birinci satirin birinci elemani, ikinci satirin ikinci elemani .. son satira kadar topla
    for ii, row in enumerate(mat):
        sum += row[ii]
    # :: 2. birinci satirin son elemani, ikinci satirin son elemani.. son satira kadar topa
    for ii in range(len(mat)-1, -1, -1):
        sum += mat[len(mat)-1-ii][ii]      # :: 44 33 22 11 00 | 04 13 22 31 40
        # print(mat[len(mat)-1-ii][ii])
    if len(mat) % 2 == 1:
        sum -= mat[len(mat)//2][len(mat)//2]

    return sum

def Main():
    # ==== test cases
    testsolo = [
               [[1,2,3],
                [4,5,6],
                [7,8,9]]
                ]
    test = [
         [[1,2,3],
          [4,5,6],
          [7,8,9]],

          [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]],

           [[5]],

           [[7,3,1,9],
            [3,4,6,9],
            [6,9,6,6],
            [9,5,8,5]]
    ]

    expected = [
        25, 8, 5, 55
    ]

    # ==== test py
    content = test
    for ii in range(len(content)):
        print("Test "  + str(ii) + " Output: " + str(solution((content[ii]))) + " Expected: " + str(expected[ii]))

# ==== Main
if __name__ == "__main__":
    Main()


