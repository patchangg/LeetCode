# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,p,q):
            if not root:
                return None
            if root == p or root == q:
                return root
            rLeft = dfs(root.left,p,q)
            rRight = dfs(root.right,p,q)

            if rLeft and rRight:
                return root
            if rLeft and not rRight:
                return rLeft
            if rRight and not rLeft:
                return rRight
        output = dfs(root,p,q)
        return output

# DFS on the tree until you find one of the nodes p or q
# If the both nodes are found on the left and right of the current node,
# that means the current node is the lowest common ancestor of both p and q
# If the left node or right node is returned with the other being empty
# that means that is the lca and return that as the other node is found below
# the p or q node meaning that it is the lca for both p and q.
# O(n), O(1) space
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 1
# output = 3
