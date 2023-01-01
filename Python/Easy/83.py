# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(head):
    if not head:
        return head
    prev = head
    curr = head
    curr = curr.next
    while curr:
        if prev.val == curr.val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head

head = [1,1,2]
# Output = [1,2]
