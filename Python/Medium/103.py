# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        for level,value in dicts.items():
            if (level % 2) == 0:
                output.append(value)
            else:
                output.append(value[::-1])
        return output

# DFS through the tree, getting every value for each level into a hashmap
# If the level is even, do nothing and append it to the List
# If the level is odd, reverse the list and then append it to the List
# O(n+m) where n is the nodes of the tree and m is the depth, O(1) space
root = [3,9,20,null,null,15,7]
# output = [[3],[20,9],[15,7]]
