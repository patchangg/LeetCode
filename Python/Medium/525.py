
def findMaxLength(nums):
    count = 0
    dicts = {0:-1}
    output = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if count in dicts:
            output = max(output, i - dicts[count])
        else:
            dicts[count] = i
    return output

# When 0 is found, -1 from the Counter, when 1 is found, +1 to the counter
# This creates a zigzag in a graph, going up and down.
# By storing the counter value, we can find two points in the graph that equal
# to that count which will be the length of the contiguous array.
# O(n), O(n) space
nums = [0,1]
maxLength = findMaxLength(nums)
print(maxLength)
