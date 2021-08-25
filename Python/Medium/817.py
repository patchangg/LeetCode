# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        output = 0
        while head:
            if head.val in nums and (head.next == None or head.next.val not in nums):
                output +=1
            head = head.next
        return output

# Check for tails in the linked list for connected components
# O(n), O(1) space
head = [0,1,2,3]
nums = [0,1,3]
# output = 2
