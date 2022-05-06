#
# ==== Binary Tree Preorder Traversal
# . Template 2.9
# . Start Date 03-Mai-2022
# . leetcode: 144
# . level : easy
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
# . +-- 10
# .     +-- 5
# .         +-- 2
# .         +-- 6  
# .     +-- 15
# .         +-- 14
# .         +-- 17


# == Libraries
import sys
from turtle import left

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
def printTree(node, tabCount=0, list=[]):
    if node == None:
        return None
    print(tabCount * '    ', '+--', node.val)
    tabCount += 1
    list.append(node.val)
    printTree(node.left, tabCount, list)
    printTree(node.right, tabCount, list)
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

def Main():
    # ==== Design
    # :: tests
    case1 = [1,None,2,3]         
    case2 = []        
    case3 = [1]
    case4 = [1,2,3]
    case5 = [10,5,2,6,15,14,17]
    case6 = [2,5,6,10,14,15,17]
    
    # :: parameter
    activeTest = case5
    #
    sogut = Tree()

    # :: set
    for ii in range(len(activeTest)):
        sogut.add(activeTest[ii])

    # :: control statements
    # print(sogut.stepMove('r'))
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
