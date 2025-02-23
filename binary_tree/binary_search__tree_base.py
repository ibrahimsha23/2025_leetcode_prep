class Tree:
    def __init__(self, root):
        self.root = root


class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = None
        self.r = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def _add_to_descendants(self, val, root):
        if val > root.val:
            if root.right is None:
                root.right = Node(val)
            else:
                self._add_to_descendants(val, root.right)
        else:
            if root.left is None:
                root.left = Node(val)
            else:
                self._add_to_descendants(val, root.left)

    def _insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add_to_descendants(val, self.root)


