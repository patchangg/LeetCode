# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        array[k-1], array[-k] = array[-k], array[k-1]
        root = ListNode(array[0])
        temp = root
        for i in range(1,len(array)):
            node = ListNode(array[i])
            root.next = node
            root = root.next
        return temp

# get the values of the linked list and then make a new array with those values
# with the index values swapped. Return the new linked list. O(2n) = O(n)
head = [7,9,6,6,7,8,3,0,9,5]
k = 5
# output = [7,9,6,6,8,7,3,0,9,5]
