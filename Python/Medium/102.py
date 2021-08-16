# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dicts = {}
        def dfs(root,level):
            if not root:
                return
            if level not in dicts:
                dicts[level] = [root.val]
            else:
                dicts[level].append(root.val)
            if root.left:
                dfs(root.left,level+1)
            if root.right:
                dfs(root.right,level+1)
        dfs(root,0)
        output = []
        for key,value in dicts.items():
            output.append(value)
        return output

# DFS Search of the tree, recording left to right the values of each level/depth
# O(n),O(1) space
root = [3,9,20,null,null,15,7]
# output = [[3],[9,20],[15,7]]
