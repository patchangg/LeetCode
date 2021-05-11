"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def maxDepth(root):
    if root is None:
        return 0

    maximum = 0
    for i in root.children:
        childHeight = self.maxDepth(i)
        maximum = max(maximum,childHeight)
    return 1+maximum


root = [1,null,3,2,4,null,5,6]
