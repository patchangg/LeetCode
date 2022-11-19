
def findMaxConsecutiveOnes(nums):
    output = 0
    curr = 0
    for num in nums:
        if num == 1:
            curr += 1
        else:
            curr = 0
        output = max(output,curr)
    return output

nums = [1,1,0,1,1,1]
maxConsecutiveOnes = findMaxConsecutiveOnes(nums)
print(maxConsecutiveOnes)
