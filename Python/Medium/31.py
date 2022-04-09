
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = j = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:
        nums.reverse()
        return
    k = i - 1
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]
    nums[i:] = nums[len(nums) - 1 : k : -1]

# Apply Generation in lexicographic order algorithm
# O(n), O(1) space
nums = [1,2,3]
nextPermutation(nums)
print(nums)
