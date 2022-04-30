#
# ==== Implementing queue using stacks
# . Template 2.9
# . Start Date 27-Apr-2022
# . leetcode: 232
# . level : easy
# . https://leetcode.com/problems/implement-queue-using-stacks/

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
# . 1 2 3 4 5 -> Array
# . 5 4 3 2 1 -> Stack1  
# . push -> 5 4 3 2 1 -> pop   | Sona erisimim yok
# .                   -> peek
# . pop, peek -> 1 2 3 4 5 -> Stack2


# . ar 1 2 3 4 5
# . s1 5 4 3 2 1
# . s2 1 2 3 4 5

# . Case 1 -> s1 de tek karakter tut
# . push 1  |  stack1      | stack2     | push+ pop+ peek+ empty+
# . push    |  stack1     |  stack2 1   | push+ pop+ peek+ empty+
# . push 2  |  stack1 2    |  stack2 1  | push+ pop+ peek+ empty+
# . push    |  stack1 2   |  stack2 1   | push+ pop+ peek+ empty+
# . push 3  |  stack1 2 |  stack2 2 1   | push+ pop+ peek+ empty+
# . push    |  stack1 3 2 |  stack2 1   | push+ pop+ peek+ empty+
# . pop     |  stack1 3   |  stack2 2   | push+ pop+ peek+ empty+

# . Case 2 -> s2 de tek karater tut
# . push 1  | stack1      |  stack2     | push+ pop+ peek+ empty+
# . push    |  stack1     |  stack2 1   | push+ pop+ peek+ empty+
# . push 2  |  stack1     |  stack2 1   | push+ pop+ peek+ empty+
# . push    |  stack1 2   |  stack2 1   | push+ pop+ peek+ empty+
# . push 3  |  stack1 3 2 |  stack2 1   | push+ pop+ peek+ empty+
# . push    |  stack1 3 2 |  stack2 1   | push+ pop+ peek+ empty+
# . pop     |  stack1 3   |  stack2 2   | push+ pop+ peek+ empty+

# . Case 3 -> 
# . push 1  | stack1      |  stack2     | push+ pop+ peek+ empty+
# . push    |  stack1     |  stack2 1   | push+ pop+ peek+ empty+
# . push 2  |  stack1     |  stack2 1   | push+ pop+ peek+ empty+
# . push    |  stack1 2   |  stack2 1   | push+ pop+ peek+ empty+
# . push 3  |  stack1 3 2 |  stack2 1   | push+ pop+ peek+ empty+
# . push    |  stack1 3 2 |  stack2 1   | push+ pop+ peek+ empty+
# . pop     |  stack1 3   |  stack2 2   | push+ pop+ peek+ empty+

# . hepsini bire pushla | peek, ilk karakteri pushla 


# == Libraries
import sys

# == Classes
class Node: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class StackLL:
    def __init__(self):
        self.head = None

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
            self.head = Node(val)
            return
        newNode = Node(val, self.head)
        self.head = newNode  

    def pop(self):
        if self.head == None:
           return
        step = self.head
        step = step.next
        self.head = step

    def peek(self):
        if self.head == None:
            return None
        return self.head.val


class MyQueue:
    def __init__(self):
        self.stackInsert = StackLL() # :: 1
        self.stackRevert = StackLL() # :: 2

    def asArray(self):
        pass

    def push(self, x: int) -> None:
        # :: ikisindede yoksa ikinciye al
        if self.stackRevert.isEmpty() and self.stackInsert.isEmpty():
            self.stackRevert.push(x)
            return
        # :: ikincide bir tane varsa ilkine at
        self.stackInsert.push(x)

    def pop(self) -> int:
        # :: ikinciyinin ilk elemanini cikar
        self.stackRevert.pop()
        # :: birincinin son cikar tut 
        while not self.stackInsert.isEmpty():
            self.stackRevert.push(self.stackInsert.peek())
            self.stackInsert.pop()
        val = self.stackRevert.peek()
        self.stackRevert.pop()
        while not self.stackRevert.isEmpty():
            self.stackInsert.push(self.stackRevert.peek())
            self.stackRevert.pop()
        # :: birinicinin son elemanini ikinciye ekle
        if val != None:
            self.stackRevert.push(val)

    def peek(self) -> int:
        return self.stackRevert.peek()

    def empty(self)  -> bool:
        return self.stackRevert.isEmpty()

# == Functions

# == Solution
def solution(head):
    pass

def Main():
    # ==== Design
    # :: tests
    testCase1 = [["MyQueue", "push", "push", "peek", "pop", "empty"],
                [[], [1], [2], [], [], []]]                                 # :: tail connects to node index 1
    testCase2 = [[1,2],0]             # :: tail connects to node index 0

    testCase3 = [1,2,3,4,5]
    
    # :: parameter
    activeTest = testCase3
    
    stack = StackLL()
    queue = MyQueue()

    # :: set
    for ii in range(0, len(activeTest)):
        queue.push(activeTest[ii])

    # ::
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    queue.pop()
    print(queue.empty())
    print(queue.peek())


    # print(queue.empty())
    # queue.push(1)
    # print(queue.empty())
    # queue.push(2)
    # queue.push(3)
    # print(queue.peek())
    # queue.pop()
    # queue.pop()
    # queue.pop()
    # print(queue.empty())

    # queue.push(4)
    # queue.push(5)
    # queue.pop()
    # print(queue.peek())
    # print(queue.asArray())
    # print("cikartildi: ", queue.pop())
    # print(queue.asArray())
    # print(stack.asArray())

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
