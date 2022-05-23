#
# ==== Fibonacci Number
# . Template 3.1
# . Start Date 21-Mai-2022
# . leetcode: 509
# . level : easy
# . https://leetcode.com/problems/fibonacci-number/

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
# . memoization: ayni isi yeniden yapiyor musun redundant work eleme
# . dynamic prgramlama konsepti 2 | memoization tabulation

# . +-- 1
# .     +-- 2
# .         +-- 3
# .         +-- 4
# .     +-- 2
# .         +-- 4
# .         +-- 3

# . traverse sol -> add
# . isim = l 
# . ['l', 'lr', 'll'] 

# . traverse sag -> kontrol
# . isim = l
# . lsitede varsa popla yoksa ekle
# . []             

# == Libraries
import sys
sys.path.append("..")
from DataStructures import StackLL
from DataStructures import BinaryTree

# == Classes

# == Functions

# == Solution
def solution(n, dict={}):           # :: o(n) solution
    # :: base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in dict:
        return dict[n]
    # :: recursive logic with memoization
    answer = solution(n-1, dict) + solution(n-2, dict)
    dict[n] = answer
    return answer 

def solutionRecursion(n):           # :: o(2**n) solution
    # :: base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # :: recursive logic
    return solution(n-1) + solution(n-2) 



def solutionIterative(n):
    # :: edge case 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    # :: 
    prev, curr = 1,1
    for ii in range(2, n):
        next = curr + prev
        prev = curr
        curr = next
    return curr

def Main():
    # ==== Design
    null = None
    # :: tests
    case1 = []         
    case2 = [1]        
    case3 = [1,2,3]
    case4 = [1,None,2,3]
    case5 = [10,5,2,6,15,14,17]
    case6 = [2,5,6,10,14,15,17]
    case7 = ["A","B","C","D","E","F","G","H","I"]
    case8 = [10,5,12,4,8,7,9,15,14]
    case9 = [3,9,20,None,None,15,7]
    case10 = [3,9,20,None,None,15,7,1,5,6,23,23]
    case11 = [1,2,None,3,None,4,None,5]
    case12 = [1,2,None,3,None,None,None,4,None,None,None,None,None,None,None,5,None]
    case13 = [1,2,2,3,4,4,3]
    case14 = [1,2,2,None,3,None,3]
    case15 = [1, null, 2]
    case16 = [2,3,3,4,null,5,4]


    # :: parameter
    # todo bunu fonksiyona tasi
    # activeTest = case11
    # for ii in range(20):
    # #     case9.append(int(5000*random()))
    # sogut = BinaryTree.BinaryTree()

    # sogut.listToBTree(case16)
    # preprintTreeNoRecursion(sogut.root)
    # print(isSymmetric(sogut.root))
    # return
    # :: set
    # for ii in range(len(activeTest)):
    #     sogut.add(activeTest[ii])

    # :: control statements
    # print(sogut.stepMove('r'))
    # print(preprintTree(sogut.root))  # . 10, 5, 4, 8, 7, 9, 12, 15, 14
    # print(preprintTreeNoRecursion(sogut.root))     # . 4, 5, 7, 8, 9, 10, 12, 14, 15
    # print(postprintTree(sogut.root)) # . 4, 7, 9, 8, 5, 14, 15, 12, 10
    
    # print(printTree(sogut.root))

    # queue.push(2)

    # return 

    # ==== test batch
    input1 = [
        0,
        3,
        4,
        5,
        6,
        7,
        14,
        30,
        40,
        60
    ]

    input2 = [

    ]

    output1 = [
        0,
        2,
        3,
        5,
        8,
        13,
        "-",
        "-",
        "-",
        "-"
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
