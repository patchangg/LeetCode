# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average = []
        def dfs(root,depth):
            if not root:
                return
            if len(average) <= depth:
                average.append([0,0])
            average[depth][0] += 1
            average[depth][1] += root.val
            if root.left:
                dfs(root.left,depth+1)
            if root.right:
                dfs(root.right,depth+1)
        dfs(root,0)
        output = []
        for avg in average:
            output.append(avg[1]/avg[0])
        return output

root = [3,9,20,null,null,15,7]
# Output = [3.00000,14.50000,11.00000]
