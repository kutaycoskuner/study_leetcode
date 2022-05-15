#
# ==== Binary Tree Level Order Traversal
# . Template 3.0
# . Start Date 13-Mai-2022
# . leetcode: 102
# . level : medium
# . https://leetcode.com/problems/binary-tree-level-order-traversal/

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
# . +-- 3                   2**0 0    
# .     +-- 9               2**1 1
# .         +-- none        2**2 1
# .         +-- none        2**2 2
# .     +-- 20              2**1 2
# .         +-- 15          2**2 3
# .         +-- 7           2**2 4

# . 
# . 0, 1, 2, 3, 4, 5,  6, 7, 8

# . 3, 9, 20, n, n, 15, 7, a, b
# . c0 c1  c1 c2 c2 c2  c2

# . 0 -> 1,2     ii*2 + 1 
# . 1 -> 3,4     ii*2 + 1
# . 2 -> 5,6     ii*2 + 1
# . 3 -> 7,8


# . 0000
# . 0001
# . 0010
# . 0100

# . 0 0  0
# . 1 1  
# . 2 1  2
# . 3 2
# . 4 2
# . 5 2
# . 6 2  6
# . 7 3
# . 8 3
# . . .  

# == Libraries
import sys
sys.path.append("..")
print(sys.path)
from  DataStructures import StackLL

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

    def listToBTree(self, list):
        # :: mapping
        mapping = {}
        # :: create root
        self.root = TreeNode(list[0])
        mapping[0] = self.root
        counter = 0
        # :: insert
        for ii in range(len(list)//2+2):   
            if list[ii] != None:
                iL = counter*2 + 1 
                iR = counter*2 + 2
                counter += 1
                if iL < len(list) and list[iL] != None:
                    newChildL = TreeNode(list[iL])
                    mapping[iL] = newChildL
                    mapping[ii].left = mapping[iL]
                if iR < len(list) and list[iR] != None:    
                    newChildR = TreeNode(list[iR])
                    mapping[iR] = newChildR
                    mapping[ii].right = mapping[iR]

    def listToBCTree(self, list):
        # :: mapping
        mapping = {}
        # :: create root
        self.root = TreeNode(list[0])
        mapping[0] = self.root
        reducer = 0
        # :: insert
        for ii in range(len(list)//2+2):   
            if list[ii] != None:
                iL = ii*2 + 1 - reducer
                iR = ii*2 + 2 - reducer
                if iL < len(list) and list[iL] != None:
                    newChildL = TreeNode(list[iL])
                    mapping[iL] = newChildL
                    mapping[ii].left = mapping[iL]
                if iR < len(list) and list[iL] != None:    
                    newChildR = TreeNode(list[iR])
                    mapping[iR] = newChildR
                    mapping[ii].right = mapping[iR]

# == Functions
def levelOrder(root):
    # :: variables
    nodeQue = []
    nodeQue.insert(0, [root, 0])  # .  3 2 1
    prevLevel = -1
    list = []
    # :: 
    while len(nodeQue) > 0:
        # :: 
        curr = nodeQue[-1]
        currNode = curr[0]
        currLevel = curr[1]
        # :: kendi ddegerini levela ekle
        if currNode != None:
            if currLevel > prevLevel:
                list.append([])
            list[currLevel].append(currNode.val)
        # :: cocuklari ekle
            if currNode.left != None:
                nodeQue.insert(0, [currNode.left, currLevel + 1])
            if currNode.right != None:
                nodeQue.insert(0, [currNode.right, currLevel + 1])
        prevLevel = currLevel                
        nodeQue.pop()
    return list
    

def printTree(node, tabCount=0, list=[]):
    if node == None:
        return None
    printTree(node.left, tabCount, list)
    print(node.val)
    list.append(node.val)
    printTree(node.right, tabCount, list)
    return list

def preprintTree(node, tabCount=0, list=[]):
    if node == None:
        return None
    print(tabCount * '    ', '+--', node.val)
    tabCount += 1
    list.append(node.val)
    preprintTree(node.left, tabCount, list)
    preprintTree(node.right, tabCount, list)
    return list

def preprintTreeNoRecursion(node, list=[]):
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
        if curr.right != None:
            nodeStack.push([curr.right, currLevel + 1])
        if curr.left != None:
            nodeStack.push([curr.left, currLevel + 1])
    return list

def postprintTree(node, tabCount=0, list=[]):
    if node == None:
        return None
    postprintTree(node.left, tabCount, list)
    postprintTree(node.right, tabCount, list)
    list.append(node.val)
    print(node.val)
    return list

# todo recursive olmadan naisl yazilabilir?

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

# inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     if root == None:
#         return []
#     list = []
#     list += self.inorderTraversal(root.left)
#     list.append(root.val)
#     list += self.inorderTraversal(root.right)
#     return list

# def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     if root == None:
#         return []
#     list = []
#     list += self.postorderTraversal(root.left)
#     list += self.postorderTraversal(root.right)
#     list.append(root.val)
#     return list

def Main():
    # ==== Design
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
    


    # .       0,1,2,   3,4,   5,6,   7
    # .                       3      
    #       

    case12 = [1,2,None,3,None,None,None,4,None,None,None,None,None,None,None,5,None]


    # :: parameter
    # todo bunu fonksiyona tasi
    # activeTest = case11
    # for ii in range(20):
    #     case9.append(int(5000*random()))
    sogut = Tree()

    sogut.listToBTree(case9)
    print(levelOrder(sogut.root))
    # preprintTreeNoRecursion(sogut.root)
    return
    # :: set
    for ii in range(len(activeTest)):
        sogut.add(activeTest[ii])

    # :: control statements
    # print(sogut.stepMove('r'))
    # print(preprintTree(sogut.root))  # . 10, 5, 4, 8, 7, 9, 12, 15, 14
    print(preprintTreeNoRecursion(sogut.root))     # . 4, 5, 7, 8, 9, 10, 12, 14, 15
    # print(postprintTree(sogut.root)) # . 4, 7, 9, 8, 5, 14, 15, 12, 10
    
    # print(printTree(sogut.root))

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
