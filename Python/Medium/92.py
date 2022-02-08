# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(head, left, right):
        if left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for n in range(left-1):
            prev = prev.next

        curr = prev.next
        nex = curr.next

        for _ in range(right-left):
            temp = nex.next
            nex.next = curr
            curr = nex
            nex = temp

        prev.next.next = nex
        prev.next = curr

        return dummy.next

# First go to the starting position to start reversing the array
# From the left position, reverse the linked list to the right position
# Connect the original head to the new reversed linked list head so that
# the non-reversed list connected to the reversed list.
# Connect the tail of the original linked list to the end of the original
# linked list. Return the head of the linked list. O(n), O(1) space 
head = [1,2,3,4,5]
left = 2
right = 4
reversedLinkedList = reverseBetween(head,left,right)
# Output = [1,4,3,2,5]
