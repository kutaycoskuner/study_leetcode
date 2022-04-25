#
# ==== Ransom Note
# . Template 2.8
# . Start Date 25-Apr-2022
# . leetcode: 383
# . level : easy
# . https://leetcode.com/problems/ransom-note/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - notlari ve resutlari temizle
# . - create test cases and test

# == Complexity Analysis
# . Time complexity       log n   | prev: n log n
# . Space Complexity

# . optimal cozumu goremiyorsan brute force
# . complexity analysis | time ve space
# . gorsellestir redundant work ara | veri yapisi | adim
# . redundancy yi kod uzerinde tespit et (pattern recognition)
# . cozum ara

# == Result
# . time    41
# . memory  54

# == Notes
# . dictionary true false ekle
# . 

# == Libraries
import sys

# == Classes

# == Functions

# == Solution
def solution(ransomNote, magazine):
    # :: ransom note un her bir karakterinin kac kere var olduguna dair bir dict tut
    dict = {}
    chars = 0
    for ii in range(len(ransomNote)):
        if not ransomNote[ii] in dict:
            dict[ransomNote[ii]] = 1
            chars += 1
        else:
            dict[ransomNote[ii]] += 1
    # :: karsilasirsan indir 
    for ii in range(len(magazine)):
        if magazine[ii] in dict:
            dict[magazine[ii]] -= 1
            if dict[magazine[ii]] == 0:
                chars -= 1
        if chars == 0:
            return True
    return False

def Main():
    # ==== test batch
    input1 = [
        "a",
        "aa",
        "aa"
    ]

    input2 = [
        "b",
        "ab",
        "aab"
    ]

    output1 = [
        False,
        False,
        True
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
