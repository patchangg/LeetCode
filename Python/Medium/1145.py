# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.leftCount = 0
        self.rightCount = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == x:
                self.leftCount = left
                self.rightCount = right
            return left + right + 1
        dfs(root)
        if (self.leftCount + self.rightCount + 1) < (n / 2):
            return True
        if (self.leftCount > (n / 2)) or (self.rightCount > (n / 2)):
            return True
        return False

# Player 2 must get more than n/2 nodes to win.
# There are 2 scenarios that player 2 wins.
# When the sum of the nodes + 1 of the node player 1 chooses is less than n / 2
# When the sum of the nodes to the left or right of the node player 1 choose
# is greater than n / 2
# All other scenarios, player 2 loses as Player 1 choose the node that has more
# nodes than any other node player 2 can choose
# O(n), O(1) space
root = [1,2,3,4,5,6,7,8,9,10,11]
n = 11
x = 3
# output = True
