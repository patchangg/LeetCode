"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

def cloneGraph(node):
    if not node:
        return node
    deepCopy = {node: Node(node.val)}
    dequeue = deque([node])
    while dequeue:
        n = dequeue.popleft()
        for neighbor in n.neighbors:
            if neighbor not in deepCopy:
                dequeue.append(neighbor)
                deepCopy[neighbor] = Node(neighbor.val)
            deepCopy[n].neighbors.append(deepCopy[neighbor])
    return deepCopy[node]

# Create a dictionary that stores a copy of the first node.
# Go through the nodes and its neighbours, creating copies of the neighbours
# if they don't exist yet in the deepCopy and create the neighbour link to
# the current copy node and append the neighbours to the deque.
# O(nlogn), O(n) space
adjList = [[2,4],[1,3],[2,4],[1,3]]
clone = cloneGraph(adjList)
# Output = [[2,4],[1,3],[2,4],[1,3]]
