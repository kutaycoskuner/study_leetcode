from DataStructures import Node

class StackLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def asArray(self):
        curr = self.head
        arr = []
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def isEmpty(self):
        return self.head == None 

    def push(self, val):
        if self.head == None:
            self.head = Node.Node(val)
            self.size += 1
            return
        newNode = Node.Node(val, self.head)
        self.head = newNode
        self.size += 1


    def pop(self):
        if self.head == None:
           return
        step = self.head
        step = step.next
        self.head = step
        self.size -= 1

    def peek(self):
        if self.head == None:
            return None
        return self.head.val