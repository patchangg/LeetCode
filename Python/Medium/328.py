# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        evenStart = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenStart
        return head

# Get the even and odd nodes into seperate listnodes and then
# at the end connect the end of the odd listnode to the start of the even
# The while loop will always end with the even pointing at a null which is good
# The even.next condition makes sure to break the loop if the number of listnodes
# is even. O(n), O(1) space
head = [1,2,3,4,5]
#output = [1,3,5,2,4]
