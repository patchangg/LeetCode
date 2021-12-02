
def triangleNumber(nums):
    nums = sorted(nums)
    output = 0
    for i in range(2,len(nums)):
        left = 0
        right = i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                output += (right - left)
                right -= 1
            else:
                left += 1
    return output

# Find two sides of a triangle that is bigger than one side of the triangle
# to get a valid triangle so sort the numbers and find any combinations that
# match that. If there is a valid set of triplets, add right - left to the
# output as there is that many possible combinations you can make from the
# numbers between the left and right number that is greater than the current
# length. O(n^2), O(n) space
nums = [2,2,3,4]
validTriangles = triangleNumber(nums)
print(validTriangles)
