# Making a linked list and exploring node based data structures.

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def Add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        
        self.count += 1

    def Delete(self, value):
        if self.count == 0:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self.count -= 1
            return True
    
        current = self.head

        while current.next != None:
            if current.next.value == value:
                current.next = current.next.next
                self.count -= 1
                return True
            else:
                current = current.next

        return False

    def GetFirstNodeWithVal(self, val):
        current = self.head
        while current != None:
            if current.value == val:
                return current
            else:
                current = current.next
        return None

    def Length(self):
        return self.count

    def Print(self):
        current = self.head
        while current != None:
            print(current.value, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.Add(1)
    linked_list.Add(5)
    print(linked_list.Length())
    linked_list.Delete(6)
    print(linked_list.Length())
    linked_list.Delete(1)
    print(linked_list.Length())
    linked_list.Delete(1)
    print(linked_list.Length())
    linked_list.Delete(5)
    print(linked_list.Length())
