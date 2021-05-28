# 4.4 Check Balanced
# Implement a function to check if a binary tree is balanced.

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def CheckBalanced(node):
    q = [node]
    while len(q) > 0:
        current = q.pop(0)
        print(f"Current is now {current.value}")
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)
        left = TraverseLeft(current)
        right = TraverseRight(current)
        print(f"Left: {left}, Right: {right}")
        if abs(left - right) > 1:
            return False
    
    return True
    
def TraverseLeft(node, depth = 0):
    if node.left != None:
        return TraverseLeft(node.left, depth + 1)
    else:
        return depth

def TraverseRight(node, depth = 0):
    if node.right != None:
        return TraverseRight(node.right, depth + 1)
    else:
        return depth
    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(8)
    root.right.left.left.left = TreeNode(9)

    print(CheckBalanced(root))
