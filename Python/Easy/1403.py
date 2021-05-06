
def minSubsequence(nums):
    array = []
    nums.sort(reverse=True)
    while sum(nums) >= sum(array):
        array.append(nums[0])
        nums.pop(0)
    return array


nums = [4,3,10,9,8]
minimum = minSubsequence(nums)
print(minimum)
