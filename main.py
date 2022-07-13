#
# ==== Libraries
from TestCases import tree
from DataStructures import Stack

# ==== Main
def Main():

    # :: change the current test function
    tree.nAryLevelOrder()
    return
    stack = Stack.Stack()


    print(len(stack.data))


    for ii in range(1, 6):
        stack.push(ii)

    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.push(12)
    print(stack.peek())
    print(stack.empty())


    

    # :: project
    # MazeSolver.run()

if __name__ == "__main__":
    Main()

# . +-- main.py

# . +-- DataStructures
# .     +-- BinaryTree.py

# . +-- TestCases
# .     +-- tree.py

# . +-- Questions
# .     +-- pathSum.py