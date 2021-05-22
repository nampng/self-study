# 2.2 Return Kth to Last
# Implement an algorithm to find the kth to last element of singly linked list.

import LinkedList

# Assuming the linked list holds a count of all elements.
def ReturnKToL(linked_list, k):
    if k > linked_list.count:
        return None
    
    current = linked_list.head
    current = TraverseToK(current, k)

    values = []
    while current != None:
        values.append(current.value)
        current = current.next
    
    return values

def TraverseToK(current, k, count = 1):
    if count == k:
        return current
    else:
        count += 1
        return TraverseToK(current.next, k, count)

# Now assume we don't know the count of the linked list.
# By placing a base case within TraverseToK_nocount, we can check whether or not k is out of bounds.
def ReturnKToL_nocount(linked_list, k):
    current = linked_list.head
    current = TraverseToK_nocount(current, k)

    values = []
    while current != None:
        values.append(current.value)
        current = current.next
    
    return values

def TraverseToK_nocount(current, k, count = 1):
    if current == None:
        return None

    if count == k:
        return current
    else:
        count += 1
        return TraverseToK_nocount(current.next, k, count)


if __name__ == "__main__":
    LL = LinkedList.LinkedList()
    LL.Add(1)
    LL.Add(2)
    LL.Add(3)
    LL.Add(4)
    LL.Add(5)

    print(ReturnKToL_nocount(LL, 5))
