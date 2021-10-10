
def deleteAndEarn(nums):
    points = [0] * 10001
    prev = 0
    curr = 0
    for num in nums:
        points[num] += num
    for point in points:
        prev, curr = curr, max(prev+point,curr)
    return curr

# Create an array that has the sum of each number in the nums array
# Go through the points array and check between the current sum and its
# adjacent sums to see which is higher. Return the highest number.
# O(n + m) n is length of nums and m is the range of nums, O(10001) space
nums = [2,2,3,3,3,4]
maximumPoints = deleteAndEarn(nums)
print(maximumPoints)
