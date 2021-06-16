# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        array = []
        def getValues(root):
            if root:
                if root.left:
                    getValues(root.left)
                array.append(root.val)
                if root.right:
                    getValues(root.right)
            else:
                return
        getValues(root)
        def makeTree(array):
            if not array:
                return None
            middle = len(array) // 2
            root = TreeNode(array[middle])
            root.left = makeTree(array[:middle])
            root.right = makeTree(array[middle+1:])
            return root

        return makeTree(array)

# In order means you have to get the most left value first
# Once you get an in order array, make a new tree with those values, starting from the middle
# There is more than 1 possible answer for the tree
# O(nLogn) as n for tree transversal, logn for splicing array
root = [1,null,2,null,3,null,4,null,null]
#output = [2,1,3,null,null,null,4]
