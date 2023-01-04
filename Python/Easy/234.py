# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isPalindrome(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    if arr == arr[::-1]:
        return True
    else:
        return False

head = [1,2,2,1]
# Output = True
