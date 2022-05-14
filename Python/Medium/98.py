# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,ceil,floor):
            if not root:
                return True
            if root.val <= floor or root.val >= ceil:
                return False
            return dfs(root.left,root.val,floor) and dfs(root.right,ceil,root.val)

        return dfs(root,float(inf),float(-inf))

# For each node in the tree, check if the node above is valid by checking if the
# nodes value is in the range between the ceiling and floor of the previous nodes
# O(n), O(1) space
root = [2,1,3]
validBST = isValidBST(root)
# Output = true
