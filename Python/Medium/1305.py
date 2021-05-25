# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.output = []
        def findAllNodes(root):
            if root is None:
                return
            self.output.append(root.val)
            findAllNodes(root.left)
            findAllNodes(root.right)
        findAllNodes(root1)
        findAllNodes(root2)
        self.output.sort()
        return self.output



root1 = [2,1,4], root2 = [1,0,3]
