
def search(nums, target):
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2

        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            return mid

    return -1

nums = [-1,0,3,5,9,12]
target = 9
indexTarget = search(nums)
print(indexTarget)
