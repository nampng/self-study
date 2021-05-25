# 4.1 Route Between Nodes
# Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

class Node:
    def __init__(self, val):
        self.value = val
        self.adj = []
        self.visited = False

# My first ever DFS. Pretty cool to see what happens when you move the nodes around.
def DFS(node, val):
    if node == None:
        return False

    print(f"Visiting {node.value}")
    node.visited

    if node.value == val:
        return True
    
    for adj in node.adj:
        if DFS(adj, val) == True:
            return True
    
    return False

if __name__ == "__main__":
    start_node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    end_node = Node(8)

    start_node.adj = [node2, node3]
    node2.adj = [node4]
    node3.adj = [node5]
    node4.adj = [node6]
    node5.adj = [end_node]
    node6.adj = [node7]

    print(DFS(start_node, 8))