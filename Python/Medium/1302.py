# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findDepth(self,root):
    if root is None:
        return 0
    else:
        leftDepth = self.findDepth(root.left)
        rightDepth = self.findDepth(root.right)

        if (leftDepth > rightDepth):
            return leftDepth+1
        else:
            return rightDepth+1

def getDeepestLeavesSum(self, root, level, height):
    if not root:
        return 0
    if level == height:
        return root.val
    return self.getDeepestLeavesSum(root.left, level+1, height) + self.getDeepestLeavesSum(root.right, level+1, height)

def deepestLeavesSum(self,root):
    maxDepth = findDepth(root)
    return self.getDeepestLeavesSum(root,1,maxDepth)

root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
