# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def convertToArray(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

        def dfs(left,right):
            if left > right:
                return None
            middle = left + (right - left) // 2
            root = TreeNode(arr[middle])
            root.left = dfs(left,middle - 1)
            root.right = dfs(middle + 1,right)
            return root

        arr = convertToArray(head)
        return dfs(0,len(arr)-1)

# Convert the linked list into an array to allow easy access to the node values
# Use the array and create the root from the middle of it and split the left and
# right sides of the middle into a sub problem
# O(n), O(n) space
head = [-10,-3,0,5,9]
# output = [0,-3,9,-10,null,5]
