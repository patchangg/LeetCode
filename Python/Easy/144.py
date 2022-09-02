# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []

        def dfs(root):
            if not root:
                return
            self.output.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return self.output

root = [1,null,2,3]
# Output = [1,2,3]
