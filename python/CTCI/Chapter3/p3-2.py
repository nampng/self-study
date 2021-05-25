# 3.2 Stack Min
# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop, and min should all operate in O(1) time.

class Stack:
    def __init__(Self):
        self.stack = []
        self.count = 0
        self.min = None

    def Push(self, val):
        self.stack.append(val)

        if self.min == None:
            self.min = val
        elif self.min > val:
            self.min = val

        self.count += 1

    def Pop(self):
        if self.count == 0:
            print("Stack is empty.")
            return
        
        val = self.stack.pop(self.count - 1)

        if self.min == val:
            self.min = self.SearchForMin(val)

        self.count -= 1

    def Peek(self):
        return self.stack[self.count - 1]
    

    def SearchForMin(self, old_min):
        # Insert searching algorithm here
        pass