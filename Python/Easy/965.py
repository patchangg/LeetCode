# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(root):
        self.flag = True

        def dfs(root,val):
            if not root:
                return
            if root.left:
                dfs(root.left,val)
            if root.right:
                dfs(root.right,val)
            if root.val != val:
                self.flag = False

        dfs(root,root.val)
        return self.flag

root = [1,1,1,1,1,null,1]
# Output = True
