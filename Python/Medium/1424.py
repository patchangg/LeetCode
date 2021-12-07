from collections import defaultdict

def findDiagonalOrder(nums):
    storage = defaultdict(list)
    output = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            storage[i+j].append(nums[i][j])
    for values in storage.values():
        for num in values[::-1]:
            output.append(num)
    return output

# Each diagonal has a specfic sum that we can use to store the diagonal values
# Loop through each array, using the index sum as a key to store the values
# and then reverse the array storing it to get the correct order and return
# the array. O(2n + m) where n is the length of nums and m is the
# longest length of a nums array, O(n) space
nums = [[1,2,3],[4,5,6],[7,8,9]]
diagonalOrder = findDiagonalOrder(nums)
print(diagonalOrder)
