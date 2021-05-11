# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(root):
        if root is None:
            return 0
        else:
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            if (left > right):
                return left+1
            else:
                return right+1

        
