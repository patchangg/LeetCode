
def partitionDisjoint(nums):
    disjoint = 0
    maxLeft = nums[0]
    currMax = maxLeft
    for i in range(len(nums)):
        currMax = max(currMax,nums[i])
        if nums[i] < maxLeft:
            disjoint = i
            maxLeft = currMax
    return disjoint + 1

# Go through each element in the nums array, keeping track of the maximum
# number currently and where to split the array. If the integer is smaller than
# the maximum left integer, update the disjoint to its position and update
# the maximum left. At the end of the loop, the disjoint should be the index
# where to split the array. O(n), O(1) space
nums = [5,0,3,8,6]
partitionLength = partitionDisjoint(nums)
print(partitionLength)
