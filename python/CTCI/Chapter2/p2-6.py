# 2.6 Palindrome
# Implement a function to check if a linked list is a palindrome.

import LinkedList

def FillStack(node, stack = []):
    if node != None:
        stack.append(node.value)
        return FillStack(node.next, stack)
    else:
        return stack

def Palindrome(head):
    stack = FillStack(head)
    current = head
    while len(stack) > 0:
        char = stack.pop()
        if current.value != char:
            return False
        else:
            current = current.next
    return True

if __name__ == "__main__":
    LL = LinkedList.LinkedList()

    LL.Add("t")
    LL.Add("a")
    LL.Add("c")
    LL.Add("o")
    LL.Add("c")
    LL.Add("a")
    LL.Add("o")

    print(Palindrome(LL.head))