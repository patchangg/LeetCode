# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = output = ListNode()
        carry = 0
        while l1 or l2 or carry:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            total += carry
            carry = total // 10
            temp = ListNode(total%10)
            dummy.next = temp
            dummy = dummy.next
        return output.next

# Create a dummy and output node, output to return the the start of the node
# and dummy to store the sum of the two nodes.
# Go through each linked list, adding the two values together and storing it
# in a new node with the value divided by 10, storing the carry for the next
# value. Link the new node to the dummy linked list and continue until there
# is no more nodes or carry value. O(n), O(max(l1,l2)) space
l1 = [2,4,3]
l2 = [5,6,4]
number = addTwoNumbers(l1,l2)
# Output = [7,0,8]
