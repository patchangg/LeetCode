# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        def dfs(root):
            if not root:
                return
            if root.val not in self.arr:
                self.arr.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        output = float(inf)
        self.arr = sorted(self.arr)
        for i in range(1,len(self.arr)):
            output = min(output,self.arr[i] - self.arr[i-1])

        return output

root = [4,2,6,1,3]
# Output = 1
