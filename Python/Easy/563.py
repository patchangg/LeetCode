# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.arr = []

        def dfs(root):
            if not root:
                return
            left = [0]
            right = [0]
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            self.arr.append(abs(sum(left)-sum(right)))
            return left + right + [root.val]
        final = dfs(root)
        return sum(self.arr)

root = [1,2,3]
# Output = 1
