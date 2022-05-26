class TreeNode: 
    def __init__(self, val=0, children=None):
        self.val = val
        if children == None:
            children = []
        self.children = children
        # for child in children:
        #     self.child = child            

class NAryTree:
    def __init__(self):
        self.root = None

    def listToTree(self, list=[]):
        # :: liste boyu buyukse
        if len(list) > 0:
            # :: N = level M = child 
            nodeQue = []
            # :: root init
            self.root = TreeNode(list[0])
            nodeQue.insert(0, self.root)
            # :: start children
            ii = 2
            while len(list) > ii:
                # :: parent node
                node = nodeQue[-1]
                # :: add children
                if list[ii] == None:
                    nodeQue.pop()
                else:
                    newNode = TreeNode(list[ii])
                    nodeQue.insert(0, newNode)
                    node.children.append(newNode)
                # :: parenti cikar | 
                ii += 1

    def preprint(self, node=-1, tabCount=0, list=[]):
        if self.root == None:
            return None
        if node == -1:
            node = self.root
        if node != None:
            print(tabCount * '    ', '+--', node.val)
            tabCount += 1
        for child in node.children:                
            self.preprint(child, tabCount, list)
