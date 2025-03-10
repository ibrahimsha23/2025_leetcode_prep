class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

preorder = [1, 2, 3]
inorder = [2, 1, 3]

class ConstructBT:

    def buildTree(self, pop_data, tree_ele):
        if tree_ele:
            latest_pop = pop_data.pop(0)
            tree_ele_index = tree_ele.index(latest_pop)
            left_tree, right_tree = tree_ele[0:tree_ele_index], tree_ele[tree_ele_index+1:]
            tree_node = TreeNode(latest_pop)
            tree_node.left = self.buildTree(pop_data, left_tree)
            tree_node.right = self.buildTree(pop_data, right_tree)
            return tree_node


cbt = ConstructBT()
cbt.buildTree(preorder, inorder)



