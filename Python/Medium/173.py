# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        temp = node.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return node.val

    def hasNext(self) -> bool:
        return self.stack

# Initiate the tree and put it into a stack. Top of the stack should be the
# smallest value in the tree
# next does a inorder traversal of the tree and returns the value of the
# node ontop of the stack
# O(1) time for next, O(h) space where h is the height of the tree
bSTIterator = BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    # return 3
bSTIterator.next();    # return 7
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 9
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 15
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 20
bSTIterator.hasNext(); # return False
