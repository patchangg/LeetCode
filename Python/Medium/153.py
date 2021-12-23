
def findMin(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Get the left and right element of the array.
# While the right element is greater than the left, find the middle index
# between the left and right index and check if that element is greater than
# the right, if so move the left index to the middle plus one else move the
# right element to the middle, this continously shortens the search until
# the smallest number is found. O(logn), O(1) space
nums = [3,4,5,1,2]
minNum = findMin(nums)
print(minNum)
