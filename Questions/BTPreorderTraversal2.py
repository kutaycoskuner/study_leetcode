#
# ==== Binary Tree Preorder Traversal
# . Template 2.9
# . Start Date 03-Mai-2022
# . leetcode: 144
# . levelStack : easy
# . https://leetcode.com/problems/binary-tree-preorder-traversal/

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
# . time    20
# . memory  61

# == Notes
# . test cases
# . ---------- Test case 1
# . []
# . ---------- test case 2
# . +-- 3
# . ---------- test case 3
# . +-- 3
# .     +-- 1
# . ---------- test case 4
# . +-- 3
# .     +-- 4
# . ---------- test case 5
# . +-- 3
# .     +-- 1
# .     +-- 4
# . ---------- test case 6
# . +-- 5                      # 0
# .     +-- 4                  # 1       
# .         +-- 3              # 2
# .     +-- 6                  # 1
# .         +-- 7              # 2
# Stack             List            Level
# [3]               []
# []                [3]              0

# [2, 5]            [3]                 
# [5]               [3, 2]           1

# [1, 5]            [3, 2]
# [5]               [3, 2, 1]        2    
# []                [3, 2, 1, 5]     1

# [4, 6]            [3, 2, 1, 5]    
# [6]               [3, 2, 1, 5, 4]  2

# == Libraries
import sys
from impQueUsingStacks import StackLL
from impQueUsingStacks import MyQueue
from random import random

# == Classes
class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            return
        curr = self.root
        prev = curr
        newNode = TreeNode(val)
        while curr != None:
            prev = curr
            if val > curr.val:
                curr = curr.right
            else: 
                curr = curr.left
        if val > prev.val:
            prev.right = newNode
        else:
            prev.left = newNode

    def delete(self, val):
        pass

    def search(self, val):
        pass

    def update(self, val):
        pass

    def stepMove(self, inst):
        # ::
        if self.root == None:
            return None
        # ::
        curr = self.root
        for ii in range(len(inst)):
            if curr == None:
                return None
            if inst[ii] == 'l':
                curr = curr.left
            if inst[ii] == 'r':
                curr = curr.right
        if curr != None:
            return curr.val
        else:
            return None

    def visualize(self):
        pass
        # :: l l r r gibi ifade yaz, o noda kadar insin dolu veya bos oldugunu yazsin
        
    def print(self):
        pass


# == Functions
def printTree2(node, tabCount=0, list=[]):
    # :: defense: check if head exists
    if node == None:
        return "no tree"
    # :: initialize traverse state
    nodeStack = MyQueue()
    nodeStack.push(node)
    # :: loop on node
    while not nodeStack.isEmpty(): 
        curr = nodeStack.peek()
        # :: do stuff with node
        list.append(curr.val)
        # :: iterate node
        nodeStack.pop()
        if curr.left != None:
            nodeStack.push(curr.left)
        if curr.right!= None:
            nodeStack.push(curr.right)
    return list

# :: non recursive
def printTree(node, list=[]):
    # :: defense: check if head exists
    if node == None:
        return "no tree"
    # :: initialize traverse state
    nodeStack = StackLL()
    nodeStack.push([node, 0]) #:: [node.val, node.level]
    # :: loop on node
    while not nodeStack.isEmpty(): 
        currArgs = nodeStack.peek()
        curr = currArgs[0]
        currLevel = currArgs[1]
        # :: do stuff with node
        print((currLevel) * '    ' ,'+--', curr.val)
        list.append(curr.val)
        # :: iterate node
        nodeStack.pop()
        if curr.right!= None:
            nodeStack.push([curr.right, currLevel + 1])
        if curr.left != None:
            nodeStack.push([curr.left, currLevel + 1])

    return list

def printTree1(node, tabCount=0, list=[]):
    if node == None:
        return None
    print(tabCount * '    ', '+--', node.val)
    tabCount += 1
    list.append(node.val)
    printTree1(node.left, tabCount, list)
    printTree1(node.right, tabCount, list)
    return list

# == Solution
# def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     if root == None:
#         return []
#     list = []
#     # print(tabCount * '    ', '+--', node.val)
#     # tabCount += 1
#     list.append(root.val)
#     list += self.preorderTraversal(root.left)
#     list += self.preorderTraversal(root.right)
#     return list

def Main():
    # ==== Design
    # :: tests
    case1 = [1,None,2,3]         
    case2 = []        
    case3 = [1]
    case4 = [1,2,3]
    case5 = [10,5,2,6,15,14,17]
    case6 = [2,5,6,10,14,15,17]
    case7 = [5,4,6,3,7]
    case8 = []

    for ii in range(20):
        case8.append(int(5000*random()))

    # :: parameter
    activeTest = case7
    #
    sogut = Tree()

    # :: set
    for ii in range(len(activeTest)):
        sogut.add(activeTest[ii])

    # :: control statements
    # print(sogut.stepMove('r'))
    print(printTree1(sogut.root))
    # print(printTree(sogut.root))
    print(printTree(sogut.root))

    # queue.push(2)

    return 

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
