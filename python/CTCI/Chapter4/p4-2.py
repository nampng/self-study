# 4.2 Minimal Tree
# Given a sorted (increasing order) array with unique elements, write an algorithm to create a binary search tree with minimal height.

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def MakeBST(array):
    if len(array) == 0:
        return
    center = int(len(array) / 2)
    print(f"{array[center]} is now a node.")

    node = Node(array[center])

    if len(array) == 1:
        return node

    node.left = MakeBST(array[:center])
    print("Added left")
    node.right = MakeBST(array[center + 1:])
    print("Added right")

    return node

def PrintLeftSide(array):
    print(f"Array length: {len(array)}")
    center = int(len(array) / 2)
    print(f"Current center: {array[center]}")
    print(array)

    if len(array) <= 1:
        return

    PrintLeftSide(array[center + 1:])


if __name__ == "__main__":
    array = list(range(0, 10))

    root = MakeBST(array)

    # PrintLeftSide(array)



