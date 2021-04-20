# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self,root,low,high):
        return traverseTree(root,low,high,0)

    def traverseTree(self,root,low,high,sum):
        if not root: # if root is empty return 0
            return 0
        if root.val >= low && root.val <= high:
            sum += root.val

        if low < root.val && root.left: # Check the left portion of the root first before high
            sum = self.traverseTree(root.left,low,high,sum)
        if high > root.val && root.right:
            sum = self.traverseTree(root.right,low,high,sum)

        return sum

root = [10,5,15,3,7,null,18]
low = 7
high = 15
sum = rangeSumBST(root,low,high)
print(sum)
