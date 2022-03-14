# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        def dfs(root,value):
            if not root:
                return 0
            l = dfs(root.left,root.val)
            r = dfs(root.right,root.val)
            self.output = max(self.output, l + r)
            if root.val == value:
                return 1 + max(l,r)
            else:
                return 0
        dfs(root,None)
        return self.output

# Go through the tree, recording if the node value is the same as the parents.
# If it is the same, increment the edge length by one, otherwise reset the path
# length. At each node, record the longest path if a new longest path is found.
# O(n), O(1) space
root = [5,4,5,1,1,5]
longestPath = longestUnivaluePath(root)
# Output = 2
