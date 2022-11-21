# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        def dfs(root):
            if not root:
                return 0
            left = right = 0
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            self.output = max(self.output,left+right)
            return max(left,right) + 1

        dfs(root)
        return self.output

root = [1,2,3,4,5]
# Output = 3
