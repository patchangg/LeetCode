from collections import defaultdict

def largestValues(root):
    self.output = defaultdict(list)
    def dfs(root,depth):
        if not root:
            return
        self.output[depth].append(root.val)
        if root.left:
            dfs(root.left,depth+1)
        if root.right:
            dfs(root.right,depth+1)
    dfs(root,0)
    result = []
    for key in self.output.keys():
        result.append(max(self.output[key]))
    return result

# Use dfs on the tree to put its value in the dictionary
# Return a list containing the  largest value in each tree level
# by using max to get the highest value in the tree level array
# O(2n) = O(n), O(1) space
root = [1,3,2,5,3,null,9]
largest = largestValues(root)
print(largest)
