# 2.3 Delete Middle Node
# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

import LinkedList

# We basically just set our node to be the next node.
# O(1)
def DeleteNode(node):
    node.value = node.next.value
    node.next = node.next.next

if __name__ == "__main__":
    LL = LinkedList.LinkedList()
    LL.Add(1)
    LL.Add(2)
    LL.Add(3)
    LL.Add(4)
    LL.Add(5)

    LL.Print()

    node = LL.GetFirstNodeWithVal(3)

    DeleteNode(node)

    LL.Print()