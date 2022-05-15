from DataStructures import Node

class LinkedList:
    def __init__(self):
        self.head = None 

    def add(self, val):
        if self.head == None:
            self.head = Node(val)
            return
        curr = self.head
        new_node = Node(val)

        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def removeVal(self, val):
        curr = self.head
        prev = self.head
        if curr.val == val:
            self.head = curr.next
            self.removeVal(val)
        while curr != None:
            # :: if curr is not head
            if curr != self.head:
                if curr.val == val:
                    prev.next = curr.next
            # :: iteration
            prev = curr
            curr = curr.next

    def get(self, index):
        curr = self.head
        for ii in range(index):
            if curr.next != None:
                curr = curr.next
            else: 
                return "list index does not exists"
        return curr.val

    def asArray(self):
        curr = self.head
        arr = []
        while curr.next != None:
            arr.append(curr.val)
            curr = curr.next
        arr.append(curr.val)
        curr = curr.next
        return arr

    def asArray(self):
        curr = self.head
        arr = []
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def connect(self, index):
        if index != None:
            curr = self.head
            target = None
            ii = 0
            while curr.next != None:
                if ii == index:
                    target = curr
                    break
                ii += 1
                curr = curr.next
            if target == None:
                target = curr
            curr.next = target

    def detectCycleSpace(self):
        # :: def: head var mi
        if self.head == None:
            return False
        # :: currenttant basla
        curr = self.head
        # :: listenin sonunu bulduuysa
        if curr.next == None:
            return False
        # :: sonuna git
        while curr != None: 
            # :: space
            seek = self.head
            if curr != seek:
                while seek != curr:
                    if curr.next == seek:
                        return curr.next.val
                    seek = seek.next
            if curr.next == curr:
                return True
            curr = curr.next
        return False

    def detectCycleTime(self):
        # :: def: head var mi
        if self.head == None:
            return False
        # :: currenttant basla
        curr = self.head
        # :: listenin sonunu bulduuysa
        if curr.next == None:
            return False
        # :: sonuna git
        kume = set()
        while curr != None: # M
            # :: kume ile
            if curr in kume:
                return True
                return "tail connects to " + str(curr.val)
            kume.add(curr)
            curr = curr.next
        return False
    