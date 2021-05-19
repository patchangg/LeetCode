# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode):
        self.totalSum = 0
        def nodeAdd(root):
            if root is None:
                return 0
            if root.right:
                nodeAdd(root.right)
            self.totalSum += root.val
            root.val = self.totalSum
            if root.left:
                nodeAdd(root.left)
        nodeAdd(root)
        return self.totalSum


# get the tree nodes in order then iterate through the order
# add their values into the total sum and replacing it
# same answer as 1038
root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
#[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
