
def getStrongest(arr, k):
    median = sorted(arr)[(len(arr)-1) // 2]
    return sorted(arr,reverse=True,key = lambda x: (abs(x-median),x))[:k]

# Get the median of the array and then use a custom sort
# The custom sort is sorted on |x-m| for each element and then reversed
# to get the strongest then we return the k strongest elements
# O(nlogn), O(n) space
arr = [1,2,3,4,5]
k = 2
strongest = getStrongest(arr,k)
print(strongest)
