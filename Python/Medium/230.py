
def kthSmallest(root, k):
    output = []
    def smallest(root):
        if root.left:
            smallest(root.left)
        output.append(root.val)
        if root.right:
            smallest(root.right)
    smallest(root)
    output.sort()
    return output[k-1]

# Do a inorder tree traversal and get every value from the tree
# Sort the tree and return the kth smallest element
# O(n) + O(n) sort = O(n), O(n) space
root = [5,3,6,2,4,null,null,1]
k = 3
smallest = kthSmallest(root,k)
print(smallest)
