# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.depth = {}
        def dfs(root,level):
            if not root:
                return
            if root.left:
                dfs(root.left,level+1)
            if root.right:
                dfs(root.right,level+1)
            if level not in self.depth:
                self.depth[level] = [root.val]
            else:
                self.depth[level].append(root.val)
        dfs(root,0)
        output = []
        for key,value in sorted(self.depth.items()):
            output.append(value)
        return output[::-1]

# Post order travel to get to the bottom of the tree. For each depth level,
# add the value into the corresponding depth level in the dictionary
# Sort the dictionary based on the key and append the values into an array
# and reverse it to get the depths values in descending order.
# O(nlogn), O(1) space
root = [3,9,20,null,null,15,7]
# output = [[15,7],[9,20],[3]]
