# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        dfs(root)

# Do a reverse pre-order transversal and remake the nodes to have the previous
# node as its right node then set the current node as previous, repeat until
# root is reached. O(n), O(1) space
root = [1,2,5,3,4,null,6]
# output = [1,null,2,null,3,null,4,null,5,null,6]
