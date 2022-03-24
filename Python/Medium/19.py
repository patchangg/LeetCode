# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# Use two pointers to get to the end of the linked list. Once the ahead pointer
# hits the end of the linked list, change the behind pointer to point to the next
# next node to remove the nth node from the linked list and return head.
# O(n), O(1) space
head = [1,2,3,4,5]
n = 2
linkedList = removeNthFromEnd(head,n)
# Output = [1,2,3,5]
