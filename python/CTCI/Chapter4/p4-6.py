# Problem 4.6 Successor

# Write an algorithm to find the "next" node of a given node in a binary search tree. 
# You may assume that each node has a link to its parents.

#       5
#   3        7
# 2   4    6   9
#            8   10

# if 3 is the chosen node, then the next successor is the right child.
# this is because the right child has no left child.
# if 4 is the chosen node, then the next successor is the parent of the parent.
# this is because there is no right child
# if 7 is chosen, then the next successor is going to be the left child of the right child.
# this is because the right child has a left child

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def NextSuccessor(node):
    # check if there is a right child.
    if node.right != None:
        # if there is right child, check for a left child
        if node.right.left != None:
            # return the left child of the right child if it exists
            return node.right.left.value
        else:
            # return the right child if the left child of the right child doesnt exist
            return node.right.value
    # if there is no right child, then we need to look for the parent or ancestor that comes next
    else:
        current = node.parent
        while current != None:
            if current.value > node.value:
                return current.value
            else:
                current = current.parent
        return None


if __name__ == "__main__":
    # Create root
    root = TreeNode(5)

    # Create first level
    root.left = TreeNode(3)
    root.right = TreeNode(7)

    # Assign parent to first level
    root.left.parent = root
    root.right.parent = root

    # Create second level
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # Assign parents to second level
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    # Create the third level
    root.right.right.right = TreeNode(10)
    root.right.right.left = TreeNode(8)

    # Assign the parent to the third level
    root.right.right.right.parent = root.right.right
    root.right.right.left.parent = root.right.right

    # Use successor function here.
    print(f"Chosen node: {root.left.value}")
    print(f"Successor node: {NextSuccessor(root.left)}")
    print(f"Chosen node: {root.left.right.value}")
    print(f"Successor node: {NextSuccessor(root.left.right)}")
    print(f"Chosen node: {root.right.value}")
    print(f"Successor node: {NextSuccessor(root.right)}")
    print(f"Chosen node: {root.value}")
    print(f"Successor node: {NextSuccessor(root)}")
    print(f"Chosen node: {root.left.left.value}")
    print(f"Successor node: {NextSuccessor(root.left.left)}")



