# Stack class
# A stack is a data structure that mainly focuses on whats on the top
# Data can only be added to the top
# Data can only be removed from the top
# Data can only be viewed from the top
# Like a stack of dinner plates.

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def Push(self, value):
        self.stack.append(value)
        self.top += 1
        return self.top

    def Pop(self):
        if self.top > -1:
            self.stack.pop()
            self.top -= 1
            return self.top
        else:
            return None
            
    def Top(self):
        if self.top > -1:
            return self.stack[self.top]
        else:
            return None

    def Count(self):
        if self.top > -1:
            return len(self.stack)
        else:
            return None