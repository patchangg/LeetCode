
def findSubarrays(nums):
    sums = []
    for i in range(len(nums)-1):
        sub = nums[i] + nums[i+1]
        if sub in sums:
            return True
        else:
            sums.append(sub)
    return False

nums = [4,2,4]
equalSubArrayExists = findSubarrays(nums)
print(equalSubArrayExists)
