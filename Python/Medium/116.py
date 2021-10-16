"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque()
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if node != None:
                node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if len(queue) > 0:
                    queue.append(None)
        return root

# Create a queue and put each root in order plus None after the level
# so that the last node in the level points to None
# If the node is none, put another None if there is another level below
# O(n + levels), O(n) space
root = [1,2,3,4,5,6,7]
# output = [1,#,2,3,#,4,5,6,7,#]
