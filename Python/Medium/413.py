
def numberOfArithmeticSlices(nums):
    total = 0
    count = 0
    for i in range(2,len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            count += 1
            total += count
        else:
            count = 0
    return total

# If the three sequential numbers have the same differences that is one count
# If the next number also has the same difference that means you can create
# two different subarrays based of the new sequence which is why we add one to count
# e.g [1,2,3] = 1 sequence, [1,2,3,4] can be [1,2,3,4] and [2,3,4] = 2
# O(n) where n is the length of nums,O(1) space
nums = [1,2,3,4]
arithmeticSlices = numberOfArithmeticSlices(nums)
print(arithmeticSlices)
