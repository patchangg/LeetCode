
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return True
        if nums[middle] < nums[right]:
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        elif nums[middle] > nums[right]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            right -= 1
    return False

# Binary search the array, checking if the array is right or left pivoted.
# O(n), O(1) space
nums = [2,5,6,0,0,1,2]
target = 0
numInArray = search(nums,target)
print(numInArray)
