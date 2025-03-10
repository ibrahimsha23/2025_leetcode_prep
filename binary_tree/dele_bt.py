class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


class BT:
    def __init__(self):
        self.root = None
        self.depth = -1


    def add_child_node(self, root, node):
        queue = [root]

        while queue:
            current_root = queue.pop(0)

            if not current_root.left:
                current_root.left = node
                return

            if not current_root.right:
                current_root.right = node
                return

            if current_root.left and current_root.right:
                queue.append(current_root.left)
                queue.append(current_root.right)
        return

    def depth_binary_tree(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            len_que = len(queue)
            self.depth += 1

            for i in range(len_que):
                c_queue = queue.pop(0)
                if c_queue.left:
                    queue.append(c_queue.left)

                if c_queue.right:
                    queue.append(c_queue.right)

    def ht_binary_tree(self, root):
        if not root:
            return 0
        return 1 + max(self.ht_binary_tree(root.left), self.ht_binary_tree(root.right))









    def add_node(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            self.add_child_node(self.root, node)


# array = [2, 3, 4, 5, 6, 7, 8, 9]
# bt = BT()
#
#
# for i  in array:
#     bt.add_node(i)


# print(bt)
# bt.depth_binary_tree()
# print(bt.depth)
# ht_tree = bt.ht_binary_tree(bt.root)
# print(ht_tree)



