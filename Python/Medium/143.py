# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        link = head.next
        while link:
            queue.append(link)
            link = link.next

        link = head
        while len(queue):
            link.next = queue.pop()
            link = link.next
            if len(queue):
                link.next = queue.popleft()
                link = link.next
        link.next = None

# Put the linked list into a deque so access to the start and end of the linked
# list is possible. While the queue is not empty, point to the end of the linked
# list then start of the linked list, until the queue is empty. O(n), O(n) space
head = [1,2,3,4]
# Output = [1,4,2,3]
