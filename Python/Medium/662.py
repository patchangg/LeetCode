# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [(root,0)]
        width = 0
        while queue:
            width = max(width,queue[-1][1] - queue[0][1] + 1)
            temp = []
            for node, level in queue:
                if node.left:
                    temp.append((node.left,level*2+1))
                if node.right:
                    temp.append((node.right,level*2+2))
            queue = temp
        return width

# Create a queue, storing each levels nodes within it.
# At the start of each level, find the maximum width from the left most to the
# right most left node and store it. Go through each node in the level and
# put their nodes in the queue. Repeat until every level is done.
# O(n), O(n) space
root = [1,3,2,5,3,null,9]
maxWidth = widthOfBinaryTree(root)
# Output = 4
