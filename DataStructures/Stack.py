#
# ==== Libraries

# ==== Classes
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        self.data.pop(-1)        

    def peek(self):
        return self.data[-1]

    def empty(self):
        return len(self.data) < 1


# ==== Functions

# ==== Variables

# ==== Main