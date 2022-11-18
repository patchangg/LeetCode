# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        def dfs(root,pos):
            if not root:
                return
            if pos > 0 and not root.right and not root.left:
                self.output += root.val
            if root.left:
                dfs(root.left,1)
            if root.right:
                dfs(root.right,0)
        dfs(root,0)

        return self.output

root = [3,9,20,null,null,15,7]
# Output = 24
