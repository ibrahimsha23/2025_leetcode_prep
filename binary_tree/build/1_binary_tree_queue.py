from PrettyPrint import PrettyPrintTree

from printer.tree import print_tree

data = [10, 20, 30, 40, 50]

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def print_tree(self):
        pass



    def add_to_descendants(self, root, val):
        queue = [root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left =  Node(val)
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right =  Node(val)
                return
            else:
                queue.append(current.right)

        pass

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.add_to_descendants(self.root, val)

    def inorder_traversal(self, node, result=None):
        """In-order traversal of the binary tree."""
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result

    def traversal(self, node, result=[]):
        if not node:
            return
        self.traversal(node.left, result)
        result.append(node.data)
        self.traversal(node.right, result)
        print(result)
        return result


if __name__ == "__main__":
    tree = BinaryTree()
    # elements = [10, 20, 30, 40, 50, 60]
    elements = ["A", "B", "C", "D", "E", "F"]
    for elem in elements:
        tree.insert(elem)
    print("Traversal data")
    print(tree.count)
    tree.traversal(tree.root)

    # print_tree(tree)
    # print("In-order Traversal of the Binary Tree:", tree.inorder_traversal(tree.root))