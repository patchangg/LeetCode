# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        j = 0
        start = ListNode()
        new = start
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                new = new.next
                l1 = l1.next
            else:
                new.next = l2
                new = new.next
                l2 = l2.next
        if l1:
            new.next = l1
        if l2:
            new.next = l2
        return start.next

list1 = [1,2,4]
list2 = [1,3,4]
# Output = [1,1,2,3,4,4]
