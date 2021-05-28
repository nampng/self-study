# 4.3 List of Depths
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

def Traverse(node, depth_dict, depth = 0):
    if depth not in depth_dict:
        depth_dict[depth] = ListNode(node.value)
    else:
        current = depth_dict[depth]
        while current.next != None:
            current = current.next
        current.next = ListNode(node.value)
    
    depth += 1

    if node.left != None:
        Traverse(node.left, depth_dict, depth)
    if node.right != None:
        Traverse(node.right, depth_dict, depth)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    #                    Tree
    #                      1
    #                  2       3
    #                4   5   6   7

    node_dict = {}
    Traverse(root, node_dict)
    for key in node_dict:
        print(f"Depth {key}:", end=" ")
        current = node_dict[key]
        while current != None:
            print(current.value, end=" ")
            current = current.next
        print()
