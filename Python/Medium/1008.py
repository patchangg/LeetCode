# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(preorder):
        root = TreeNode(preorder[0])
        preorder = preorder[1:]
        def addNode(root,val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    addNode(root.left,val)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    addNode(root.right,val)
        for num in preorder:
            addNode(root,num)
        return root



preorder = [8,5,1,7,10,12]
