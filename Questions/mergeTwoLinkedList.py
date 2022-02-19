#
# ==== Merge Two Sorted Lists
# :: Template 1.7
# :: leetcode: 21
# :: https://leetcode.com/problems/merge-two-sorted-lists/

# == Procedure
# :: - template edit if any
# :: - change title
# :: - change leetcode number
# :: - link of the question
# :: - create test cases and test

# == Complexity Analysis
# :: M ..

# == Notes
# :: - linked list ist linear collection of data elements whose order is not given by their physical in memory.


# == Classes
# :: Definition for singly-linked list.
from re import A


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # :: head i tanimliyorsun
    
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
    
    def merge(self, list):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = list.head
 
    def sort(self):
        if self.head == None:
            return
        # print(self.asArray())
        curr = self.head
        while curr.next != None:
            next = curr.next
            if curr.val > next.val:  
                curr.val = int(curr.val) + int(next.val)               
                next.val = int(curr.val) - int(next.val)                  
                curr.val = int(curr.val) - int(next.val) 
                curr = self.head   
                continue              
            curr = curr.next
        return self.head

# == Functions
def solution(list1,list2):
    

    a = [-2,5]
    b = [-9,-6,-3,-1,1,6]

    listA = LinkedList()
    listB = LinkedList()

    # todo
    for ii, jj in enumerate(a):
        listA.add(a[ii])     
    for ii, jj in enumerate(b):
        listA.add(b[ii])     
    # todo


    # listA = LinkedList(list1)
    # listB = LinkedList(list2)

    # list1.merge(list2)
    # list1.sort()
    # print(list1.asArray())

    listA.merge(listB)
    listA.sort()

    print(listA.asArray())
    return 0

def Main():
    # ==== test cases
    testsolo = [
               [[1,2,3],
                [4,5,6],
                [7,8,9]]
                ]
                
    test1 = [
        [1,2,4],
        [],
        []
    ]

    test2 = [
        [1,3,4],
        [],
        [0]
    ]

    expected = [
        [1,1,2,3,4,4],
        [],
        [0]
    ]

    # ==== test py
    content = [2]
    # for ii in range(len(content)):
    #     print("Test "  + str(ii) + " Output: " + str(solution((content[ii]))) + " Expected: " + str(expected[ii]))
        
    for ii in range(len(content)):
        print("Test "  + str(ii) + " Output: " + str(solution(test1[ii],test2[ii])) + " Expected: " + str(expected[ii]))

# ==== Main
if __name__ == "__main__":
    Main()


