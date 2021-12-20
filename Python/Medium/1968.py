
def rearrangeArray(nums):
    nums = sorted(nums)
    for i in range(1,len(nums),2):
        nums[i],nums[i-1] = nums[i-1],nums[i]
    return nums

# Sort the array and swap each pair of numbers so that each number will have
# neighbours that are either smaller than it or larger than it which would make
# the average of the two not equal to itself. O(nlogn), O(n) space
nums = [6,2,0,9,7]
nonEqualNeighbours = rearrangeArray(nums)
print(nonEqualNeighbours)
