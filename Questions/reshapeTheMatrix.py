#
# ==== Reshape the Matrix
# . Template 2.6
# . Start Date 21-Apr-2022
# . leetcode: 566
# . level : easy
# . https://leetcode.com/problems/reshape-the-matrix/

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
# . dictionary index | value
# . dictionary ye ekle
# . onceki indexleri current value dan cikar eger daha yuksekse o indexi tut

# == Libraries
import sys

# == Classes

# == Functions

# == Solution
def solution(mat, r, c):
    newMat = []                     # . yeni matris
    rc, cc = -1, 0                  # . row count; column count
    # :: rowa gir
    for ii in range(len(mat)):
        # :: kolona gir
        for jj in range(len(mat[ii])):
            # :: row ekle
            if cc == 0:
                newMat.append([])
                cc = c
                rc += 1
            # :: kolon ekle
            if cc != 0:
                newMat[rc].append(mat[ii][jj])
                cc -= 1
    # :: return
    return newMat if rc == r-1 and cc == 0 else mat

def Main():
    # ==== test batch
    input1 = [
        [[1,2],[3,4]],
        [[1,2],[3,4]],
        [[1,2],[3,4]]
    ]
    input2 = [
        1,
        2,
        4
    ]
    input3 = [
        4,
        4,
        1
    ]

    output1 = [
        [[1,2,3,4]],
        [[1,2],[3,4]],
        [[1],[2],[3],[4]]
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
                str(solution(input1[ii], input2[ii], input3[ii])) + "\t Expected: " + str(output1[ii]))
    else:
        print("Test " + str(args) + " Output: " +
                str(solution(input1[args-1], input2[args-1], input3[args-1])) + "\t Expected: " + str(output1[args-1]))


# ==== Main
if __name__ == "__main__":
    Main()
