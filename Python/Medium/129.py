# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root,total):
            if not root:
                return
            total += str(root.val)
            if root.left:
                dfs(root.left,total)
            if root.right:
                dfs(root.right,total)
            if not root.left and not root.right:
                arr.append(int(total))
        dfs(root,"")
        return sum(arr)

# DFS through the tree, where you keep adding the value of the leaf as a string
# onto a total string. Once it hits the bottom of the tree, add the total as
# an integer into an array. Once all the bottom nodes have been hit, return
# the sum of the totals. O(n), O(1) space
root = [1,2,3]
# output = 25
