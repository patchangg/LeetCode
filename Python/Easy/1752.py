
def check(nums):
    k = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            k += 1
        if k > 1:
            return False
    return True

nums = [3,4,5,1,2]
isSortedArray = check(nums)
print(isSortedArray)
