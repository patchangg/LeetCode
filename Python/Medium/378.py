
def kthSmallest(matrix, k):
    output = []
    for arr in matrix:
        output += arr
    output = sorted(output)
    return output[k-1]

# Combine all the arrays, sort it and get the kth smallest element
# O(nlogn), O(n) space
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
smallest = kthSmallest(matrix,k)
print(smallest)
