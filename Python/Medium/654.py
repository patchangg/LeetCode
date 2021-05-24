# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(nums):
        if not nums:
            return None
        stack = []
        last = None
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                last = stack.pop()
            if stack:
                stack[-1].right = node
            if last:
                node.left = last
            stack.append(node)
            last = None
        return stack[0]

nums = [3,2,1,6,0,5]

# stack = [3]
# stack = [3,2] 3.right = 2
# stack = [3,2,1] 2.right = 1
# stack = [] last = 3 6.left = 3
# stack = [0]
# stack = [] 5.left = 0
#
# nums = [3,2,1]
# stack = [3]
# stack = [3,2] 3.right = 2
# stack = [3,2,1] 2.right = 1

# works since the stack will contain numbers smaller than the largest
# so we use that to make those nodes lined together then eventually
# it will be the left of the largest node
#
