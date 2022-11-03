
def countHillValley(nums):
    output = 0
    j = 0
    for i in range(1,len(nums)-1):
        if (nums[j] < nums[i] and nums[i] > nums[i+1]) or (nums[j] > nums[i] and nums[i] < nums[i+1]):
            output += 1
            j = i
    return output

nums = [2,4,1,1,6,5]
numHillsAndValleys = countHillValley(nums)
print(numHillsAndValleys)
