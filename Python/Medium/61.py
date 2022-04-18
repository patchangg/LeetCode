# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        length = 1
        firstNode = head

        while firstNode.next:
            firstNode = firstNode.next
            length += 1

        k = k % length

        firstNode.next = head

        lastNode = head

        for _ in range(length - k - 1):
            lastNode = lastNode.next

        output = lastNode.next
        lastNode.next = None
        return output

# Loop to the end of the linked list, getting the length and make the final
# node point to the head of the linked list. Move to length - k node to start
# the rotation to the right by making that node point to none. This will get
# a right rotated array. O(n+k) where n is the length of the linked list and
# k is length - k, O(1) space. 
head = [1,2,3,4,5]
k = 2
linkedList = rotateRight(head,k)
# Output = [4,5,1,2,3]
