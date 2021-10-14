# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(root):
        if root is None:
            return True
        queue = []
        flag = False
        queue.append(root)
        while(len(queue) > 0):
            temp = queue.pop(0)
            if (temp.left):
                if flag == True :
                    return False
                queue.append(temp.left)
            else:
                flag = True
            if (temp.right):
                if flag == True:
                    return False
                queue.append(temp.right)
            else:
                flag = True
        return True

# Create a queue and check do in order transversal of the tree
# If the node is not a full node, each node after must be a leaf node.
# Raise a flag to true, and if the rest of the nodes are leaves, return True.
# If the left node is empty than the right node also must be empty or it is
# not a complete tree else return false
# O(n), O(n) space
root = [1,2,3,4,5,6]
# output = true
