# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right,root.val)
        return root

# Go through the nodes, until the node is found. Once found swap it out with its
# left or right node or swap the values with its right node and keep going
# left until the last node which is be used as the replacement, then delete
# the replacement node afterwards. O(h), O(1) space
root = [5,3,6,2,4,null,7]
key = 3
# Output = [5,4,6,2,null,null,7]
