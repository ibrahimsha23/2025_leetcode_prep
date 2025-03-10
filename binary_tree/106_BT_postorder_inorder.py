class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]

class ConstructBT:

    def buildTree(self, pop_data, tree_ele):
        if tree_ele:
            latest_pop = pop_data.pop(-1)
            tree_ele_index = tree_ele.index(latest_pop)
            left_tree, right_tree = tree_ele[0:tree_ele_index], tree_ele[tree_ele_index+1:]
            tree_node = TreeNode(latest_pop)
            tree_node.right = self.buildTree(pop_data, right_tree)
            tree_node.left = self.buildTree(pop_data, left_tree)
            return tree_node


cbt = ConstructBT()
a = cbt.buildTree(postorder, inorder)
print(a)



