# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []

        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            self.output.append(root.val)

        dfs(root)
        return self.output

root = [1,null,2,3]
# Output = [3,2,1]
