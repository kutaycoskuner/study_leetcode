#
# ==== N-Ary Tree Level Order Traversal
# . Template 3.2
# . Start Date 26-Mai-2022
# . leetcode: 429
# . level : medium
# . https://leetcode.com/problems/n-ary-tree-level-order-traversal/

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

# == Libraries
import sys
sys.path.append("..")
from DataStructures import StackLL
from DataStructures import BinaryTree

# == Classes

# == Functions

# == Solution
def solution():
    pass

def levelOrder(root):
    # :: defensive root var mi?
    if root == None:
        return []
    # :: variables
    node = root
    nodeQue = []
    list = [[node.val]]
    # :: init state 
    nodeQue.insert(0, [node, 0]) # :: insert node, level
    # :: insert children 
    while len(nodeQue) > 0:
        node = nodeQue[len(nodeQue)-1][0]
        level = nodeQue[len(nodeQue)-1][1]
        for ii in range(len(node.children)):
            # :: yeni row varsa yeni liste ekle
            if level + 1 >= len(list):
                list.append([])
            # :: node u que ya ekle
            nodeQue.insert(0, [node.children[ii], level+1])
            # :: ilgili seviyenin listesine ekle
            list[level+1].append(node.children[ii].val)
        nodeQue.pop()
    return list


def Main():
    # ==== Basic Testing
    input1 = [
        0,
        3,
        4
    ]

    output1 = [
        0,
        2,
        3
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
