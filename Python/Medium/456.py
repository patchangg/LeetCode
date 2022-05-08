
def find132pattern(nums):
    stack = []
    mid = float(-inf)
    for num in nums[::-1]:
        if num < mid:
            return True
        while stack and stack[-1] < num:
            mid = stack.pop()
        stack.append(num)
    return False

# Create a stack, if the last number of the stack is smaller than the current
# number, it becomes the new middle / k / 3 number. If the next number in the
# array is smaller than the middle, that means there is a 132 pattern in the
# array and return True. O(n), O(n) space
nums = [1,2,3,4]
oneTwoThree = find132pattern(nums)
print(oneTwoThree)
