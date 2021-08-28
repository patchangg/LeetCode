"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        stack = [head]
        prev = Node(0)
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            prev = root
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
                root.child = None
        head.prev = None
        return head

# Create a stack and go through the linked list
# Each linked list, update the next and previous and add the next to the stack
# Check if the node has a child before moving to the next node as we need to
# go through the child first. Append the child to the stack and change the node
# to point to nothing for child.
# O(n) where n is the number of nodes, O(1) space
head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# output = [1,2,3,7,8,11,12,9,10,4,5,6]
