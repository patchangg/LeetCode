# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def rsv(root,depth):
            if not root:
                return
            if len(output) <= depth:
                output.append(root.val)
            if root.right:
                rsv(root.right,depth+1)
            if root.left:
                rsv(root.left,depth+1)
        rsv(root,0)
        return output

# Do a pre order travel but right first instead of left.
# Check if a entry for the depth level is in the output or not to determine
# if it is the most right node in the tree
# O(n), O(1) space
root = [1,2,3,null,5,null,4]
# output = [1,3,4]
