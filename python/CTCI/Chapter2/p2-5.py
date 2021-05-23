# 2.5 Sum Lists
# You have numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and return the sum as a linked list.

# Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2)
# Output: (2 -> 1 -> 9)

import LinkedList

def SumUp(node1, node2, linked_list, carry = 0):
    if node1 == None and node2 == None:
        return
    
    sum = carry

    if node1 != None:
        sum += node1.value
        node1 = node1.next
    if node2 != None:
        sum += node2.value
        node2 = node2.next

    carry, sum = divmod(sum, 10)

    linked_list.Add(sum)
    SumUp(node1, node2, linked_list, carry)

# FOLLOW UP
# If what if the digits were forwards?

if __name__ == "__main__":
    list1 = LinkedList.LinkedList()
    list2 = LinkedList.LinkedList()
    list_solution = LinkedList.LinkedList()

    list1.Add(7)
    list1.Add(1)
    list1.Add(6)
    list1.Add(5)
    list1.Add(2)

    list1.Print()

    list2.Add(5)
    list2.Add(9)
    list2.Add(2)

    list2.Print()

    SumUp(list1.head, list2.head, list_solution)

    list_solution.Print()