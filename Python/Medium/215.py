
def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]

# Use built in sort and get the kth largest element.
# O(nlogn), O(1) space
nums = [3,2,3,1,2,4,5,5,6]
k = 4
kthlargest = findKthLargest(nums,k)
print(kthlargest)
