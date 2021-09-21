# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.array = []
        while head:
            self.array.append(head.val)
            self.counter += 1
            head = head.next


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.array)

# Store the linked list values in a array
# When getRandom is called, select a random element from the array by
# selecting a random int from 0 to length of the array and then return it
# O(n), O(1) space for init and getRandom
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
