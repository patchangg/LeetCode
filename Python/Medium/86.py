# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode()
        start = smaller
        larger = ListNode()
        end = larger
        while head:
            if head.val < x:
                smaller.next = ListNode(head.val)
                smaller = smaller.next
            else:
                larger.next = ListNode(head.val)
                larger = larger.next
            head = head.next
        smaller.next = end.next
        return start.next

# Go through the linked list, storing the values into two seperate linked lists
# Once the loop has ended, combine the two seperate linked list and return
# the head. O(n), O(1) space
head = [1,4,3,2,5,2]
x = 3
# Output = [1,2,2,4,3,5]
