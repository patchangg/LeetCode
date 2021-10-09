# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root or depth <= 0:
            return None
        if depth == 1:
            return TreeNode(val,root,None)
        if depth == 2:
            root.left = TreeNode(val,root.left,None)
            root.right = TreeNode(val,None,root.right)
        else:
            root.left == self.addOneRow(root.left,val,depth-1)
            root.right == self.addOneRow(root.right,val,depth-1)
        return root

# Do a dfs until we reach depth == 2 which then add one row to the tree
# O(n), O(1) space
root = [4,2,6,3,1,5]
val = 1
depth = 2
# output = [4,1,1,2,null,null,6,3,1,5]
