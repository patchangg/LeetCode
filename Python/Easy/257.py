# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.output = []
        def dfs(root,path):
            if not root.left and not root.right:
                path += str(root.val)
                self.output.append(path)
                return
            else:
                path += str(root.val) + "->"
                if root.left:
                    dfs(root.left,path)
                if root.right:
                    dfs(root.right,path)
        dfs(root,"")
        return self.output

root = [1,2,3,null,5]
# Output = ["1->2->5","1->3"]
