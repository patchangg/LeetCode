
def maximumTop(nums, k):
    length = len(nums)
    if k == 0:
        if length >= 1:
            return nums[0]
        else:
            return -1
    if k == 1:
        if length == 1:
            return -1
        else:
            return nums[1]
    if length == 1:
        if k % 2 == 0:
            return nums[0]
        else:
            return -1

    output = -1
    for i in range(min(length, k-1)):
        output = max(output, nums[i])

    if k < length:
        output = max(output, nums[k])

    return output

# If the number of moves is 0, return the first number if it exists
# If the number of moves is 1 and the length of the array isn't one, return the
# second element as if the length is only one, the array will be empty.
# If the length of the array is one, k must be a even number to return the
# element back as odd numbers will make the array empty
# Otherwise go through the array until k index, finding the largest number
# and compare it with the next number to check if putting the maximum number
# back in is the optimal move. O(n), O(1) space
nums = [5,2,2,4,0,6]
k = 4
maximumTopElement = maximumTop(nums,k)
print(maximumTopElement)
