# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next
            else:
                prev.next = curr.next

            curr = curr.next
        return dummy.next

# Create a dummy node that points to head so we can return to it
# Use two pointers, prev and curr to keep track of the non duplicate nodes
# If duplicate value nodes are found, skip them until the last one.
# Once we reach a non duplicate node, set the previous next to point to it
# and keep going through the linked list. This will remove the duplicate
# nodes from getting pointed at. O(n), O(1) space
head = [1,2,3,3,4,4,5]
nonDuplicateLinkedList = deleteDuplicates(head)
# Output = [1,2,5]
