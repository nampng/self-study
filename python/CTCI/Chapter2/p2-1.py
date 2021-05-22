# 2.1 Remove Dups
# Write code to remove duplicates from an unsorted linked list.

# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# This solution fails to check for duplicates when another duplicate is found.
# Look for a recursive approach?
def RemoveDups_failed(linked_list):
    val_dict = {}
    current = linked_list.head
    val_dict[current.value] = 1
    while current != None:
        if current.next.value in val_dict:
            current.next = current.next.next
        else:
            val_dict[current.next.value] = 1
        current = current.next

# Solution uses recursion.
# Sucessfully checks for sequential duplicates
def RemoveDups(current, val_dict = {}):
    if current not in val_dict:
        val_dict[current.value] = 1
    
    if current.next == None:
        return
    
    if current.next.value in val_dict:
        current.next = current.next.next
        RemoveDups(current, val_dict)
    else:
        val_dict[current.next.value] = 1
        current = current.next
        RemoveDups(current, val_dict)

# Taken from Structures/LinkedList.py
# ------------------------------------------------------------
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

    def Length(self):
        return self.count

    def Print(self):
        current = self.head
        while current != None:
            print(current.value, end=" ")
            current = current.next
        print()
# ------------------------------------------------------------

if __name__ == "__main__":
    linlis = LinkedList()
    linlis.Add(1)
    linlis.Add(2)
    linlis.Add(3)
    linlis.Add(1)
    linlis.Add(2)
    linlis.Add(2)
    linlis.Add(3)
    linlis.Add(1)
    linlis.Add(4)
    linlis.Add(4)
    linlis.Add(5)
    linlis.Add(4)
    linlis.Add(4)
    linlis.Add(6)
    linlis.Add(4)
    linlis.Add(7)

    linlis.Print()

    RemoveDups(linlis.head)

    linlis.Print()