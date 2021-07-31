# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        output = []
        self.dicts = {}
        def dfs(root):
            l = 0
            r = 0
            if root.left:
                l = dfs(root.left)
            if root.right:
                r = dfs(root.right)
            value = l + r + root.val
            if value in self.dicts:
                self.dicts[value] += 1
            else:
                self.dicts[value] = 1
            return value
        dfs(root)
        maxValue = max(self.dicts.items(), key=lambda x: x[1])
        for key,value in self.dicts.items():
            if value == maxValue[1]:
                output.append(key)
        return output

# Get the subtree sum for each node in the tree
# Find the highest frequency and append the values that have the highest frequency
# O(n + n + nlog(n)) = O(nlog(n)) where n is the amount of nodes in the tree, O(1) space
root = [5,2,-5]
# output = [2]
