# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            odd = prev.next
            even = odd.next
            prev.next, odd.next, even.next = even, even.next, odd
            prev = odd
        return start.next

# Create a start node which gets the start of the linked list and prev node
# which starts at the even node
# Swap the even and odd nodes in the linked list until we can't swap
# any more pairs and then return the start.next which should be the new
# head of the linked list. O(n), O(1) space
head = [1,2,3,4]
# output = [2,1,4,3]
