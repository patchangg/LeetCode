# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left:
            root.left = self.removeLeafNodes(root.left,target)
        if root.right:
            root.right = self.removeLeafNodes(root.right,target)
        if root.left == root.right and root.val == target:
            return None
        else:
            return root

# dfs search until the node has no left or right children
# if the leaf is equal to the target, return None so that it links to None
# once the node checks children, it will check itself to see if it has become a
# leaf node, check if value, remove if so. Repeat for whole tree
# O(N) as it looks through the tree once
root = [1,2,3,2,null,2,4]
target = 2
#output = [1,null,3,null,4]
