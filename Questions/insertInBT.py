#
# ==== Insert in Binary Search Tree
# . Template 3.2
# . Start Date 24-Mai-2022
# . leetcode: 701
# . level : medium
# . https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
def searchBST(root, val: int):
        # :: defensive
        if root == None:
            return None
        if root.val == val:
            return root
        # :: search
        return searchBST(root.left, val) if root.val > val else searchBST(root.right, val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        newNode = TreeNode(val)
        # :: base
        if root == None:
            root = newNode
            return root
        
        # :: arama
        while node != None:
            if node.val >= val:
                if node.left == None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if node.right == None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right     
        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         # :: base
#         if root == None:
#             root = TreeNode(val)
#             return root
#         # :: ekleme
#         if root.val > val:
#             if root.left == None:
#                 root.left = TreeNode(val)
#                 return root
#             else: 
#                 self.insertIntoBST(root.left, val)        
#         else: 
#             if root.right == None:
#                 root.right = TreeNode(val)
#                 return root
#             else: 
#                 self.insertIntoBST(root.right, val)
#         return root

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
