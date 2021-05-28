# 4.5 Validate BST
# Implement a function to check if a binary tree is a binary search tree.

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None

def CheckBST(root):
    q = [root]
    while len(q) != 0:
        current = q.pop(0)
        if current.left != None:
            if current.left.value > current.value:
                return False
            else:
                q.append(current.left)
        if current.right != None:
            if current.right.value < current.value:
                return False
            else:
                q.append(current.right)
    return True

if __name__ == "__main__":
    root = Node(6)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.left = Node(7)
    root.right.right = Node(9)

    #           6
    #       4       8
    #     2   5   7   9

    print(CheckBST(root))
