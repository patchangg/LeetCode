"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.output = []
        if not root:
            return []

        def recursion(root):
            for child in root.children:
                recursion(child)
            self.output.append(root.val)

        recursion(root)
        return self.output

root = [1,null,3,2,4,null,5,6]
# Output = [5,6,3,2,4,1]
