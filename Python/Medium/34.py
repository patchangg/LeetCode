
def searchRange(nums, target):
    i = 0
    j = len(nums) - 1
    output = [-1,-1]
    if not nums:
        return output
    while i < j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        else:
            j = mid
    if nums[i] == target:
        output[0] = i
    else:
        return output

    j = len(nums) - 1
    while i < j:
        mid = ((i + j) // 2) + 1
        if nums[mid] > target:
            j = mid - 1
        else:
            i = mid

    output[1] = j
    return output

# Do two binary searches to find the left and right position of the target in
# the array. The first binary search finds the left position and uses the left
# position as the anchor for the right. O(logn), O(1) space
nums = [5,7,7,8,8,10]
target = 8
targetPositions = searchRange(nums,target)
print(targetPositions)
