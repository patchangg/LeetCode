
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0,nums[-1])
        nums.pop()

# Put the last number at the front then pop the array. O(n*k), O(1) space
nums = [1,2,3,4,5,6,7]
k = 3
rotatedArray = rotate(nums,k)
