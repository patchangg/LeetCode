
def wiggleMaxLength(self, nums: List[int]) -> int:
    up = None
    output = 1
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1] and up != False:
            output += 1
            up = False
        elif nums[i] > nums[i-1] and up != True:
            output += 1
            up = True
    return output

# Cannot sort the array. Check if the second element is greater or smaller than
# the previous, this will determine is the pattern is positive or negative first
# Check if it is increasing or decreasing and if the wiggle pattern needs it.
# If so, add one to the output and flip the boolean. O(n), O(1) space
nums = [1,7,4,9,2,5]
maxLength = wiggleMaxLength(nums)
print(maxLength)
