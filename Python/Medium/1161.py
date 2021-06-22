# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        nodeVal = {}
        def findSum(root,level):
            if not root:
                return None
            if level in nodeVal:
                nodeVal[level] += root.val
            else:
                nodeVal[level] = root.val
            findSum(root.left,level+1)
            findSum(root.right,level+1)
        findSum(root,1)
        return max(nodeVal.items(), key=operator.itemgetter(1))[0]

# Go through each level of the tree and add the values of each levels' nodes
# return key with the maximum value in the dictionary. O(n)
root = [989,null,10250,98693,-89388,null,null,null,-32127]
#output = 2
