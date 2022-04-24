#
# ==== First Unique Character in String
# . Template 2.7
# . Start Date 24-Apr-2022
# . leetcode: 387
# . level : easy
# . https://leetcode.com/problems/first-unique-character-in-a-string/

# == Result
# . time    71
# . memory  61

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
# . dictionary true false ekle
# . halihazirda varsa false a cevir
# . true varsa return

# == Libraries
import sys

# == Classes

# == Functions

# == Solution
def solution(s):
    # :: dictionary true false ekle
    dict = {}
    for ii in range(len(s)):
        if not s[ii] in dict:
            dict[s[ii]] = ii
        else:
            dict[s[ii]] = -1
    # :: halihazirda varsa false a cevir
    for key, val in dict.items():
        if val != -1:
            return val
    return -1
    

def Main():
    # ==== test batch
    input1 = [
        "leetcode",
        "loveleetcode",
        "aabb"
    ]

    output1 = [
        0,
        2,
        -1
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
            # print(str((solution(input1[ii]) == output1[ii])))
    else:
        answer = solution(input1[args-1])
        print("Test " + str(args) + " Output: " +
                str(answer) + "\t Expected: " + str(output1[args-1]) + '\n' + str(answer == output1[args-1]))


# ==== Main
if __name__ == "__main__":
    Main()
