
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] >= nums[left]:
            if nums[left] <= target and target < nums[right]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if nums[right] < target and target <= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
    return -1

# Binary search but check if the array is left or right pivoted.
# O(logn), O(1) space
nums = [4,5,6,7,0,1,2]
target = 0
targetIndex = search(nums,target)
print(targetIndex)
