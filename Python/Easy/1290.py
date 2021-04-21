# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getDecimalValue(head):
    node = head
    String = ""
    while node is not None:
        String = String + str(node.val)
        node = node.next
    decimal = int(number,2)
    return decimal

head = [1,0,1]
base10 = getDecimalValue(head)
print(base10)
