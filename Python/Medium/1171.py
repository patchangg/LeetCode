# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        hashmap = {0:dummy}
        while head:
            prefix += head.val
            hashmap[prefix] = head
            head = head.next

        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = hashmap[prefix].next
            head = head.next
        return dummy.next

# Calculate the prefix sum of the linked list and put it in a hashmap
# This allows the linked list to act as a array where we can skip the sections
# that sum up to 0. Since there is two passes, use a dummy node to go back
# to the start of the linked list once the prefix sum has been calculated.
# Using the prefix sum, connect the occurances of the prefix sum from the hashmap
# so no zero sum sublists exist. O(n), O(n) space
head = [1,2,-3,3,1]
nonZeroSumLinkedList = removeZeroSumSublists(head)
# Output = [3,1]
