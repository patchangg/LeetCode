# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        self.answer = None
        def find(node):
            if node.val == target.val:
                self.answer = node
            else:
                if node.left:
                    find(node.left)
                if node.right:
                    find(node.right)
        if cloned != None:
            find(cloned)
        return self.answer

tree = [7,4,3,null,null,6,19]
target = 3
