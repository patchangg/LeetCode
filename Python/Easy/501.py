from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counted = Counter()

        def dfs(root):
            if not root:
                return
            counted[root.val] += 1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        mc = []
        maxCt = counted.most_common(1)[0][1]
        for item,val in counted.items():
            if val == maxCt:
                mc.append(item)
        return mc

root = [1,null,2,2]
# Output = [2]
