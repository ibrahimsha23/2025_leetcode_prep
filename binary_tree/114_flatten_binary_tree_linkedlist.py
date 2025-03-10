from dele_bt import BT

def flatten(root):
    if not root:
        return None
    l, r = root.left, root.right
    flatten(l)
    if l:
        root.left = None
        root.right = l
        tail_right_node =  root.right
        while tail_right_node.right != None:
            tail_right_node = tail_right_node.right
        tail_right_node.right = r
    flatten(r)
    return


# array = [1, 2, 5, 3, 4, None, 6]
array = [1, 2, 5, 3, 4, None, 6]

bt = BT()


for i  in array:
    bt.add_node(i)

flatten(bt.root)
print(bt)


