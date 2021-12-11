
def minIncrementForUnique(nums):
    level = -1
    output = 0

    for num in sorted(nums):
        if level < num:
            level = num
        else:
            level += 1
            output += level - num
    return output

# Sort the numbers. Level is the unique number we give to each position in the
# array so it will be unique. If the current num is greater than the level,
# that means it is unique, otherwise we raise the level and take the difference
# between the level and the current level in order to make it unique.
# O(nlogn), O(n) space
nums = [3,2,1,2,1,7]
minIncrement = minIncrementForUnique(nums)
print(minIncrement)
