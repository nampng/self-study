# 2.4 Partition
# Write code to partition a linked list around a value x, such that all nodes less than x come before
# all nodes greater than or equal to x.

import LinkedList
import random

# O(N)?
def Partition(linked_list, pivot):
    current = linked_list.head
    steps = 0
    while current != None:
        steps += 1
        while current.next != None and current.next.value < pivot:
            steps += 1
            hold = current.next
            current.next = current.next.next
            old_head = linked_list.head
            linked_list.head = hold
            linked_list.head.next = old_head
        current = current.next
    
    print(f"Total steps: {steps}")

if __name__ == "__main__":
    LL = LinkedList.LinkedList()
    for i in range(100):
        LL.Add(random.randint(0, 100))

    LL.Print()

    Partition(LL, 50)

    LL.Print()
    