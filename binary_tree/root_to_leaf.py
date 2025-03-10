class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Function to collect paths
def collect_paths(node, path, paths):
    if node is None:
        return

    # Append this node to the path
    path.append(node.data)

    # If it's a leaf node, store the path
    if node.left is None and node.right is None:
        paths.append(list(path))
    else:

        # Otherwise, try both subtrees
        collect_paths(node.left, path, paths)
        collect_paths(node.right, path, paths)

    # Backtrack: remove the last element from the path
    path.pop()


# Function to get all paths from root to leaf
def paths(root):
    paths = []
    collect_paths(root, [], paths)
    return paths


if __name__ == "__main__":

    # Constructed binary tree is
    #        10
    #       /   \
    #      8     2
    #     / \   /
    #    3   5 2
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    paths = paths(root)
    for path in paths:
        print(" ".join(map(str, path)))
