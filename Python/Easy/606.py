# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        output = str(root.val)

        if root.left:
            output += "(" + self.tree2str(root.left) + ")"

        if not root.left and root.right:
            output += "()"

        if root.right:
            output += "(" + self.tree2str(root.right) + ")"

        return output

root = [1,2,3,4]
# Output = "1(2(4))(3)"
