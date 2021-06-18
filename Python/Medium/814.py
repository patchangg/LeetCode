# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)
        if root.left == root.right and root.val != 1:
            return None
        else:
            return root

# dfs search until the node has no left or right children
# if the leaf does not equal 1, return None so that it links to None
# once the node checks children, it will check itself to see if it has become a
# leaf node, check if value, remove if so. Repeat for whole tree
# O(N) as it looks through the tree once
root = [1,null,0,0,1]
#output = [1,null,0,null,1]
