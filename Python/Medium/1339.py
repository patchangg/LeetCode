# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        total = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.output = max(self.output, left * (total - left), right * (total - right))
            return left + right + root.val

        total = dfs(root)
        dfs(root)
        return self.output % (10**9 + 7)

# Get the total sum of all the nodes first
# Go through each node, doing post order transversal to get the sum of the
# left and right sub trees and compare the product compared to the current
# maximum. O(n), O(n) space
root = [1,2,3,4,5,6]
# Output = 110
