#
# ==== Pascal Triangle
# . Template 2.6
# . Start Date 21-Apr-2022
# . leetcode: 118
# . level : easy
# . https://leetcode.com/problems/pascals-triangle/

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
def solution(n, tri=[[1]]):
    # :: edge case
    if n == 1:
        return tri
    # :: base case

    # :: recursive logic
    row = [1,1]
    lastRow = tri[len(tri)-1]
    if len(lastRow) > 1:
        for ii in range(len(lastRow)-1):
            row.insert(-1,lastRow[ii] + lastRow[ii+1])
    tri.append(row)
    return solution(n-1, tri)


def solutionIterative(numRows):
    newRow = [1]
    pascal = [[1]]
    iteration = 1
    # :: newRow kadar iterasyon 
    for ii in range(numRows-1):
        newRow = [1]
        for yy in range(iteration): # . 1 2 1     
            # :: son eleman yoksa 1 ekle
            if yy+1 >= iteration:
                newRow.append(1)
            # :: 1,2; 2,3; 3,4; topla insert et
            else:
                item = pascal[-1][yy] + pascal[-1][yy+1]
                newRow.append(item)
        iteration += 1
        # :: pascal a ekle
        pascal.append(newRow)
    # :: 1 2 1 
    return pascal

def Main():
    # ==== test batch
    input1 = [
        1,
        2,
        3,
        5
    ]

    output1 = [
        [[1]],
        [[1],[1,1]],
        [[1],[1,1],[1,2,1]],
        [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
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
                str(solution(input1[ii])) + "\t Expected: " + str(output1[ii]))
            print(str((solution(input1[ii]) == output1[ii])))
            print(type(solution(input1[ii])), type(output1[ii]))

    else:
        answer = solution(input1[args-1])
        print("Test " + str(args) + " Output: " +
                str(answer) + "\t Expected: " + str(output1[args-1]) + '\n' + str(answer == output1[args-1]))


# ==== Main
if __name__ == "__main__":
    Main()
