
def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1

    start = 1
    end = len(nums) - 2

    while start <= end:
        middle = (start + end) // 2

        if nums[middle] > nums[middle + 1] and nums[middle - 1] < nums[middle]:
            return middle
        elif nums[middle] < nums[middle - 1]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

# Check if the start or end element of the array is a peak element
# otherwise binary search from index 1 to n - 2 and check if the middle
# element is peak or not. O(logn), O(1) space
nums = [1,2,3,1]
peakElement = findPeakElement(nums)
print(peakElement)
