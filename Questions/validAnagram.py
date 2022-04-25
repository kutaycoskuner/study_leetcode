#
# ==== Valid Anagram
# . Template 2.8
# . Start Date 25-Apr-2022
# . leetcode: 242
# . level : easy
# . https://leetcode.com/problems/valid-anagram/

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
# . time    
# . memory  

# == Notes
# . size kontrol et
# . s yi dict yap her bir karakteri gir
# . ikinciden her bir karakteri cikar

# == Libraries
import sys

# == Classes

# == Functions

# == Solution
def solution(s, t):
    # :: s yi dict yap her bir karakter sayisi kadar val ata
    dict = {}
    chars = 0
    if len(s) == len(t):
        for ii in range(len(s)):
            if not s[ii] in dict:
                dict[s[ii]] = 1
                chars += 1
            else:
                dict[s[ii]] += 1
        # :: ikinciden her bir karakteri cikar
        for ii in range(len(t)):
            if t[ii] in dict:
                dict[t[ii]] -= 1
                if dict[t[ii]] == 0:
                    chars -= 1
            if chars == 0:
                return True
    return False

def Main():
    # ==== test batch
    input1 = [
        "anagram",
        "rat",
        "aykut"
    ]

    input2 = [
        "nagaram",
        "car",
        "kutay"
    ]

    output1 = [
        True,
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
