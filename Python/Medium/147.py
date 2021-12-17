# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()

        curr = head
        while curr:
            sortedCurr = output
            while sortedCurr.next and curr.val >= sortedCurr.next.val:
                sortedCurr = sortedCurr.next
            temp, sortedCurr.next = sortedCurr.next, curr
            curr = curr.next
            sortedCurr.next.next = temp

        return output.next

# Create a dummy head node used to attach the sorted linked List
# Go through the linked list, looking for the next largest value that is bigger
# than the value in the dummy linked list and find where to place it in there.
# Do this for every element in the linked list and return the next node after the
# dummy head for the sorted list. O(n^2), O(1) space
head = [4,2,1,3]
# Output = [1,2,3,4]
