# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = None
        last = list1
        for i in range(b+1):
            if i == a - 1:
                first = last
            last = last.next
        first.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = last
        return list1
