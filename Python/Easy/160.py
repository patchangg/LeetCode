# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getIntersectionNode(headA, headB):

    pa = headA
    pb = headB

    while pa != pb:
        if pa:
            pa = pa.next
        else:
            pa = headB
        if pb:
            pb = pb.next
        else:
            pb = headA
    return pa

intersectVal = 8
listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
skipA = 2
skipB = 3
intersectionNode = getIntersectionNode(headA,headB)
# Output = Intersected at '8'
