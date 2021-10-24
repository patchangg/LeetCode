# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0,0)
            left = dfs(root.left)
            right = dfs(root.right)
            return (root.val + left[1] + right[1], max(left[0],left[1]) + max(right[0],right[1]))
        return max(dfs(root))

# Do a dfs on the binary tree and find out for each node, is it better to rob
# them now or rob the nodes below them. So for every node, we find the value
# of robbing them and the value of robbing the child or skipping them
# At the root of the tree, it will contain all the values of robbing the root
# and the children nodes it would of robbed if robbed now compared to robbing
# the root child and the child you rob after. O(n), O(1) space
root = [3,2,3,null,3,null,1]
# output = 7
