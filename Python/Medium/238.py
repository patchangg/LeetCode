
def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
    for i in range(1,n):
        output[i] = output[i-1] * nums[i-1]
    rightP = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * rightP
        rightP = rightP * nums[i]
    return output

# To find the product of all the elements of nums exculding the ith index
# we just calculate the elements to the left and right of the ith index
# The first loop we calculate everything to the left, second loop to the right
# O(2n) where n is the length of nums = O(n), O(1) space
nums = [1,2,3,4]
product = productExceptSelf(nums)
print(product)
