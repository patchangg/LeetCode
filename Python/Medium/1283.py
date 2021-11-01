
def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    left = 1
    right = max(nums)
    while left < right:
        middle = (left + right) // 2
        if sum((middle + i - 1) // middle for i in nums) > threshold:
            left = middle + 1
        else:
            right = middle
    return left

# Binary Search
# Search between 1 and the largest number in nums, dividing the array by the
# middle of the two numbers and if the result is greater than the threshold
# the change the left to the middle + 1 and if it is smaller than the threshold,
# change right to the middle. Repeat until the left is greater or equal to the
# right. O(nlogM) where M is max(nums), O(1) space
nums = [1,2,5,9]
threshold = 6
divisor = smallestDivisor(nums,threshold)
print(divisor)
