# Use this script to transfer hand written code to computer

class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1

    def Push(self, val):
        self.stack.append(val)
        self.count += 1

    def Pop(self):
        if self.count > -1:
            val = self.stack[self.count]
            self.stack.pop(self.count)
            self.count -= 1
            return val

class Queue:
    def __init__(self):
        self.queue = []
        self.count = 0
    
    def Enqueue(self, val):
        self.queue.append(val)
        self.count += 1
    
    def Dequeue(self):
        if self.count > 0:
            self.queue.pop(0)
            self.count -= 1

class LinkedListNode:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.count = 0

    def Append(self, val):
        new_node = LinkedListNode(val)
        if self.count == 0:
            self.head = new_node
            self.count += 1
            return
        
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        self.count += 1
        return
    
    def Insert(self, val, pos):
        new_node = LinkedListNode(val)
        if pos > self.count - 1 or pos < 0:
            return
        
        if pos == 0:
            if self.head == None:
                self.head = new_node
                self.count += 1
                return
            else:
                new_node.next = self.head
                self.head = new_node
                self.count += 1
                return
        
        current = self.head
        for i in range(1, pos):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.count += 1

    def Remove(self, val):

        if self.count == 0:
            return
        
        if self.head.value == val:
            self.head = self.head.next
            self.count -= 1
            return

        current = self.head.next
        while current.next != None:
            if current.next.value == val:
                current.next = current.next.next
                self.count -= 1
                return
            else:
                current = current.next

    def TraversePrint(self):
        print()
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print()

if __name__ == "__main__":
    # l = LinkedList()
    # l.Append(1)
    # l.Append(2)
    # l.Append(3)
    # l.Append(4)
    # l.TraversePrint()
    # l.Insert(5, 2)
    # l.TraversePrint()
    # l.Remove(3)
    # l.TraversePrint()
    # l.Remove(4)
    # l.TraversePrint()
    # l.Insert(3, 2)
    # l.Insert(4, 3)
    # l.TraversePrint()

    pass