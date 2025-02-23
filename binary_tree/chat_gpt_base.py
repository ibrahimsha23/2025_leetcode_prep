# Define the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define the BinaryTree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a value into the binary tree
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
        else:
            # Duplicate values are not inserted
            print(f"Value {value} already exists in the tree.")

    # In-order traversal (Left, Root, Right)
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)
        return result

    # Pre-order traversal (Root, Left, Right)
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    # Post-order traversal (Left, Right, Root)
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.value)
        return result

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for elem in elements:
        tree.insert(elem)

    print("In-order Traversal:", tree.in_order_traversal(tree.root))
    print("Pre-order Traversal:", tree.pre_order_traversal(tree.root))
    print("Post-order Traversal:", tree.post_order_traversal(tree.root))