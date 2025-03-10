from dele_bt import BT

def colection_paths(node, path, paths):
    if not node:
        return None
    path.append(node.data)
    colection_paths(node.left, path, paths)
    colection_paths(node.right, path, paths)
    if not node.left and not node.right:
        paths.append(sum(path))

    path.pop()

    return paths


# array = [1, 2, 5, 3, 4, None, 6]
array = [10, 8, 2, 3, 5, 2]

bt = BT()


for i  in array:
    bt.add_node(i)

result = colection_paths(bt.root, [], [])
print(result)



