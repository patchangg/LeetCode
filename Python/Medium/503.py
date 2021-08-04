
def nextGreaterElements(nums):
    stack = []
    output = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            output[stack.pop()] = nums[i]
        stack.append(i)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            output[stack.pop()] = nums[i]
        if stack == []:
            break
    return output

# Use two loops, one for the current array and another for a circular array
# First array checks if any number ahead is greater than the index ontop of the stack
# If so replace the output with that number
# The second loop checks again to see if any previous numbers before the index
# is greater than it, if so replace it. O(n), O(n) space
nums = [1,2,3,4,3]
greaterElements = nextGreaterElements(nums)
print(greaterElements)
