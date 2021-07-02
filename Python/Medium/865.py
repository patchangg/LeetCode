# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root):
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]

# Do a post order transversal to get the bottom of the tree
# We try to find the height that is the lowest and return a subtree
# That only contains the deepest leafs inside
# So we compare the height of each node, return the subtree that has the
# deepest leaves. If subtree contains a right and left child with the
# deepest leaves, return that as the root of the subtree. 
root = [3,5,1,6,2,0,8,null,null,7,4]
# output = [2,7,4]
