# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        dicts = {}
        def dfs(root,level):
            if not root:
                return True
            if level % 2 == 0 and root.val % 2 == 0:
                return False
            if level % 2 == 1 and root.val % 2 == 1:
                return False
            if not level in dicts:
                dicts[level] = [root.val]
            else:
                if (level % 2) == 0:
                    if root.val <= dicts[level][-1]:
                        return False
                else:
                    if root.val >= dicts[level][-1]:
                        return False
                dicts[level].append(root.val)
            return dfs(root.left,level+1) and dfs(root.right,level+1)
        return dfs(root,0)

# DFS on the tree, check if the numbers are even on the odd-indexed levels
# and odd on the even-indexed levels. Add the value into the level index
# in the hashmap to compare with the other values
# For even level values, they must be strictly increasing from left to righ
# and odd level values must be strictly decreasing from left to right
# If we hit the bottom of the tree, return True as it matched all the criterias
# O(n), O(n) space
root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# output = true
