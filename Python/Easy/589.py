"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def preorder(self, root: 'Node') -> List[int]:
    preorder = []
    self.recurse(root,preorder)
    return preorder

def recurse(self,root,preorder):
    if root is None:
        return preorder
    preorder.append(root.val)
    for i in root.children:
        self.recurse(root,preorder)

root = [1,null,3,2,4,null,5,6]
