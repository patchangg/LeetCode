
def maxProduct(nums):
    maxProd = nums[0]
    minProd = nums[0]
    output = nums[0]
    for i in range(1,len(nums)):
        newMax = max(nums[i],maxProd*nums[i],minProd*nums[i])
        newMin = min(nums[i],maxProd*nums[i],minProd*nums[i])
        maxProd = newMax
        minProd = newMin
        output = max(output,maxProd)
    return output

# For each number in the array, calculate the highest positive and negative
# seen currently as a product can use two negative numbers to get an even
# higher positive number. O(n), O(1) space
nums = [2,3,-2,4]
number = maxProduct(nums)
print(number)
