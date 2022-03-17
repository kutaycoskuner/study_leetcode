#
# ==== Swap Nodes in Pairs
# . Template 2.1
# . leetcode: 24
# . level : medium
# . https://leetcode.com/problems/swap-nodes-in-pairs/

# == Procedure
# . - template edit if any
# . - change title
# . - change leetcode number
# . - link of the question
# . - create test cases and test

# == Complexity Analysis
# Time complexity
# Space Complexity

# == Notes

# == Classes
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

    def connect(self, index):
        if index == None:
            return "connected to None"
        curr = self.head
        target = None
        ii = 0
        while curr.next != None:
            if ii == index:
                target = curr
            ii += 1
            curr = curr.next
        curr.next = target
        return "connected to " + str(target.val)

    def detectCycle(self):
        if self.head == None:
            return None
        curr = self.head
        kume = set()
        if curr.next == None:
            return None
        while curr.next != None: # M
            if(curr.next in kume):
                # print('test')
                return "tail connects to " + str(curr.val)
            kume.add(curr)
            curr = curr.next
        return None

    def swapPairs(self):
        # . 1> 2> 3> 4> 5> 6x
        # . c  o
        # . 2= 1> 3> 4> 5> 6x
        # . o  c  
        # . 2> 1> 3> 4> 5> 6x
        # . o  c
  
        # . 2> 1= 3> 4> 5> 6x
        # .    p  c  o       
        # . 2> 1> 4> 3> 5> 6x
        # .       o  c
        # . 2> 1> 4> 3> 5> 6x
        # .    p     c


        # :: cift ise oncekini gosterecek
        # :: onceki sonrakini gosterecek
        curr = self.head
        if curr.next != None:
            odd = curr.next
        else:
            return
        # :: ikinciyi head yap
        if odd != None:
            self.head = odd
        
        while curr.next != None:
            if curr.next != None:
                # :: 2n-1 oncekini sonrakine bagla
                curr.next = odd.next
                # :: 2n simdikini oncekine bagla
                odd.next = curr
            next = curr.next
            prev = curr
            if next != None:
                curr.next = next.next
                curr = next
                odd = curr.next
        if odd != None:
            odd.next = curr
        else: 
            prev.next = curr
        curr.next = None        
        return ("curr val: ", curr.val, " odd val:", prev.val)


                


# == Functions

# == Libraries
    
    
def solution(head):
    pass

def Main():
    # ==== test solo
    listDataA = [1,2,3,4,5 ]             # :: 2,1,4,3
    listDataB = [[1,2],0]             # :: tail connects to node index 0
    listDataC = [[1], None]                 # :: no cycle

    listData = listDataA
    listA = LinkedList()

    for ii in range(0, len(listData)):
        listA.add(listData[ii])

    print(listA.asArray())
    print(listA.swapPairs())
    print(listA.asArray())
    # print(listA.connect(listData[1]))
    # print(listA.detectCycle())

    
    # ==== test batch
    test1 = [
            ["9001 discuss.leetcode.com"],
            ["900 google.mail.com", "900 intel.mail.com"],
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
        ]

    expected1 = [
        ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"],
        ["900 google.mail.com", "900 intel.mail.com", "1800 mail.com", "1800 com"],
        ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    ]

    # ==== test solo
    # print(solution(test0))
    # for ii in range(len(test0)):
    #     print("Test "  + str(ii+1) + " Output: " + str(solution(test0[ii])))

    # ==== test batch
    # for ii in range(2,3): # len(test1)
    #     print("Test "  + str(ii+1) + " Output: " + str(solution(test1[ii])) + " Expected: " + str(expected1[ii]))

    # ==== test specific
    # for ii in range(len(test1)):
    #     print("Test "  + str(ii) + " Output: " + str(solution(test1[ii],test11[ii])) + " Expected: " + str(expected1[ii]))



# ==== Main
if __name__ == "__main__":
    Main()





