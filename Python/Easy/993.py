# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xd = -1
        self.yd = 0
        self.xp = -2
        self.yp = -3

        def dfs(root,depth,parent):
            if not root:
                return
            if root.val == x:
                self.xd = depth
                self.xp = parent
            if root.val == y:
                self.yd = depth
                self.yp = parent
            if root.left:
                dfs(root.left,depth + 1,root.val)
            if root.right:
                dfs(root.right,depth + 1,root.val)
        dfs(root,0,0)
        return self.xd == self.yd and self.xp != self.yp

root = [1,2,3,4]
x = 4
y = 3
# Output = false
