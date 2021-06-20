# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = 0
        def findMax(node,maxVal,minVal):
            if not node:
                self.result = max(self.result,maxVal-minVal)
                return
            findMax(node.left,max(node.val,maxVal),min(node.val,minVal))
            findMax(node.right,max(node.val,maxVal),min(node.val,minVal))
        findMax(root,0,1000000)
        return self.result

# DFS Search of the tree, we keep track of the max and min values of the nodes
# while going down the tree, once it has hit a null node, check the result
# repeat until we hit all the leaf children and return the result of the
# maximum anscestor differnce. abs could of have been used but no null values given
# Look through tree + leaf children so O(n) time complexity
#root = [8,3,10,1,6,null,14,null,null,4,7,13]
#output = 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
