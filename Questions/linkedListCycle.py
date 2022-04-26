#
# ==== Linked List Cycle
# . Template 2.8
# . Start Date 26-Apr-2022
# . leetcode: 141
# . level : easy
# . https://leetcode.com/problems/linked-list-cycle/

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
# . a b c d e
# .     s c
# . a b c d e

# == Libraries
import sys

# == Classes
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None 

    def add(self, val):
        if self.head == None:
            self.head = ListNode(val)
            return
        curr = self.head
        new_node = ListNode(val)

        while curr.next != None:
            curr = curr.next
        curr.next = new_node

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

# . a b c d e
# .     s c
# . a b c d e

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
    

# == Functions

# == Solution
def solution(s, t):
    pass

def Main():
    # ==== Design tests
    # :: [[linked list node items], cycle connection]
    listDataA = [[3,2,0,-4],3]        # :: tail connects to node index 1
    listDataB = [[1,2],0]             # :: tail connects to node index 0
    listDataC = [[1], -1]             # :: no cycle
    listDataD = [[-1,-7,7,-4,19,6,-9,-5,-2,-5], 9]


    listData = listDataA
    listA = LinkedList()

    for ii in range(0, len(listData[0])):
        listA.add(listData[0][ii])

    # print(listA.asArray())
    listA.connect(listData[1])
    print(listA.detectCycleTime())
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
