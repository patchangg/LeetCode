# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.totalSum = 0
        def dfs(root,parents):
            if not root:
                return
            if len(parents) > 1:
                if (parents[0] % 2) == 0:
                    self.totalSum += root.val
                parents.pop[0]
            dfs(root.left,parents + [root.val])
            dfs(root.right,parents + [root.val])
        dfs(root,[])
        return self.totalSum



# keep a track of parent and grandparents value
# compare nodes that have depth 2+ / parents > 2 as they are the only ones with parent and grandparents
# if grandparent is even (gp % 2 ) == 0, then add node value to output
# new depth, pop grand parent, add node as parent
root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
