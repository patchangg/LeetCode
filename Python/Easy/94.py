# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.array = []
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            self.array.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return self.array

root = [1,null,2,3]
# Output = [1,3,2]
