# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.r1 = []
        self.r2 = []

        def dfs(root,w):
            if not root:
                return
            if not root.left and not root.right:
                if w == 1:
                    self.r1.append(root.val)
                elif w == 2:
                    self.r2.append(root.val)
            if root.left:
                dfs(root.left,w)
            if root.right:
                dfs(root.right,w)
        dfs(root1,1)
        dfs(root2,2)
        if self.r1 == self.r2:
            return True
        else:
            return False

root1 = [3,5,1,6,2,9,8,null,null,7,4]
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
isLeafsSimilar = leafSimilar(root1,root2)
# Output = True
