# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.arr = []
        self.root = root
        self.root.val = 0
        def recover(root):
            if root.left:
                self.arr.append((2 * root.val) + 1)
                root.left.val = (2 * root.val) + 1
                recover(root.left)
            if root.right:
                self.arr.append((2 * root.val) + 2)
                root.right.val = (2 * root.val ) + 2
                recover(root.right)
        recover(self.root)

    def find(self, target: int) -> bool:
        if target in self.arr:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
