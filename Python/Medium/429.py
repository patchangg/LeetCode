"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levelDict = {}
        def findOrder(root,level):
            if not root:
                return None
            if level in levelDict:
                levelDict[level].append(root.val)
            else:
                levelDict[level] = [root.val]
            for i in root.children:
                findOrder(i,level+1)
        findOrder(root,0)
        output = []
        for key,value in levelDict.items():
            output.append(value)
        return output

# For each level, put its nodes values into a dictionary and loop through each nodes children
# Once all values have been added, place from top to bottom the levels values into a list and return it
# O(n) + O(n) = O(2n) = O(n)
root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#output = [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
