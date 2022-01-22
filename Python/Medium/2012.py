
def sumOfBeauties(self, nums: List[int]) -> int:
    minArr = [0 for j in range(len(nums))]
    maxArr = [0 for k in range(len(nums))]
    minNum = float('-inf')
    maxNum = float('inf')
    output = 0

    for j in range(len(nums)):
        minArr[j] = minNum
        minNum = max(nums[j],minNum)

    for k in range(len(nums)-1,-1,-1):
        maxArr[k] = maxNum
        maxNum = min(maxNum,nums[k])

    for i in range(1,len(nums)-1):
        if minArr[i] < nums[i] < maxArr[i]:
            output += 2
        elif nums[i - 1] < nums[i] < nums[i + 1]:
            output += 1

    return output

# To deal with the first case of num[j] < num[i] < num[k], store the smallest
# num at i from 0 to i - 1 and highest num from i + 1 to n - 1
# If nums[i] is between those numbers, add 2 to the total
# otherwise check if nums[i - 1] < nums[i] < nums[i + 1] for 1 point
# O(n), O(n) space
nums = [1,2,3]
beauties = sumOfBeauties(nums)
print(beauties)
