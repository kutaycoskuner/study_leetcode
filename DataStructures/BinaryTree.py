class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
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
        if len(list) > 0:
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

    def preprint(self, node=-1, tabCount=0, list=[]):
        if self.root == None:
            return None
        if node == -1:
            node = self.root
        if node != None:
            print(tabCount * '    ', '+--', node.val)
            tabCount += 1
            self.preprint(node.left, tabCount, list)
            self.preprint(node.right, tabCount, list)

    def preorderList(self, node=-1, tabCount=0, list=[]):
        if self.root == None:
            return None
        if node == -1:
            node = self.root
        if node != None:
            list.append(node.val)
            self.preorderList(node.left, tabCount, list)
            self.preorderList(node.right, tabCount, list)
            return list