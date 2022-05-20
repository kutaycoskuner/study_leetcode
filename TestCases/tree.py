from DataStructures import BinaryTree
from Questions import maximumDepthofBT
from Questions import invertBT as x



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

def runTests_maxDepthTree():
    sogut = BinaryTree.BinaryTree()
    sogut.listToBTree(case12)
    print(x.levelOrder(sogut.root))
    print(x.maxDepth(sogut.root) == x.maxDepthRecursive(sogut.root))
    return 

def runTests_invertBT():
    mese = BinaryTree.BinaryTree()
    mese.listToBTree(case5)
    print(x.preprintTree(mese.root,[]))
    x.invertBT(mese.root)
    print(x.preprintTree(mese.root,[]))
    return
