# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0
        maximum = root.val
        def goodNode(root,maximum):
            if root:
                if root.val > maximum:
                    maximum = root.val
                    self.output += 1
                elif root.val == maximum:
                    self.output += 1
                goodNode(root.left,maximum)
                goodNode(root.right,maximum)
        goodNode(root,maximum)
        return self.output


root = [3,1,4,3,null,1,5]
