# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.output = root.val
        self.maxDepth = 0
        def lowestDepth(root,depth,side):
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.output = root.val
            if root.left:
                lowestDepth(root.left,depth+1,1)
            if root.right:
                lowestDepth(root.right,depth+1,0)
        lowestDepth(root,0,0)
        return self.output

# Use inner function to find the lowest left node value by doing a preorder
# traversal of the tree. Since we go left first, that ensures that the
# most left node will be found first rather than a right node on the same level
# O(n) where n is the amount of nodes in tree, O(1) space
root = [1,2,3,4,null,5,6,null,null,7]
