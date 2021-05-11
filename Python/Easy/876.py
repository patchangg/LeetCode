# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        counter = 0
        copyed = head
        while copyed is not None:
            counter += 1
            copyed = copyed.next
        if (counter % 2) == 0:
            middle = -(-counter//2)
        else:
            middle = counter/2

        for i in range(int(middle)):
            head = head.next
        return head

node = [1,2,3,4,5]
middle = middleNode(node)
print(middle)
