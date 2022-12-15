
def pivotIndex(nums):
    left = 0
    right = sum(nums)
    for i,n in enumerate(nums):
        right -= n
        if left == right:
            return i
        left += n
    return -1

nums = [1,7,3,6,5,6]
pivot = pivotIndex(nums)
print(pivot)
