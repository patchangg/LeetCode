# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1val = ""
        l2val = ""
        while l1:
            l1val += str(l1.val)
            l1 = l1.next
        while l2:
            l2val += str(l2.val)
            l2 = l2.next
        output = list(str(int(l1val)+int(l2val)))
        if output:
            head = ListNode(int(output[0]))
            start = head
            for i in range(1,len(output)):
                head.next = ListNode(int(output[i]))
                head = head.next
            return start
        return []

# Get the two numbers from the two linked lists and add them together
# Transform that number into a list and create a LinkedList with nodes containing
# each digit in the number. O(n+m+(n+m)) = O(n), O(n+m) space
l1 = [7,2,4,3]
l2 = [5,6,4]
# output = [7,8,0,7]
