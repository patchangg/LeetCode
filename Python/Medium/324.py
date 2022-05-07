
def wiggleSort(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    n = len(nums[::2])
    nums[::2], nums[1::2] = nums[:n][::-1], nums[n:][::-1]

# Get the middle of the sorted array. Put the smaller half on even numbers and
# the larger half on odd numbers. Each half puts the numbers from largest to
# smallest. O(nlogn), O(n) space
nums = [1,5,1,1,6,4]
nums = wiggleSort(nums)
print(nums)
