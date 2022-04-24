
def findUnsortedSubarray(nums):
    n = len(nums)
    sArray = sorted(nums)
    start = 0
    end = n - 1
    while start < n and nums[start] == sArray[start]:
        start += 1
    while end > start and nums[end] == sArray[end]:
        end -= 1
    return end - start + 1

# Create a sorted array of nums. Create a starting and ending point in the
# original array and find the index where the sorted and unsorted arrays don't
# match. This will find the starting and ending points of the subarray that
# can be sorted in ascending order as the two points should only contain
# numbers smaller than the last point and greater than the starting point.
# O(nlogn), O(n) space
nums = [2,6,4,8,10,9,15]
subarray = findUnsortedSubarray(nums)
print(subarray)
