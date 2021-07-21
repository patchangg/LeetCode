
def waysToMakeFair(nums):
    arr1 = [0, 0]
    arr2 = [sum(nums[0::2]), sum(nums[1::2])]
    output = 0
    for i, num in enumerate(nums):
        arr2[i % 2] -= num
        output += arr1[0] + arr2[1] == arr1[1] + arr2[0]
        arr1[i % 2] += num
    return output

# Use the prefix sum trick on the odd and even indices
# Iterate through the nums array
# we can get the even sum after removing num from the even or odd position in the second array
# Even sum comes from the remaining odd numbers + even current, vise versa for odd
# if they equal, that means they are a fair and add one to the output
# O(n), O(1) space
nums = [2,1,6,4]
fairArrays = waysToMakeFair(nums)
print(fairArrays)
