
def findDisappearedNumbers(nums):
    n = len(nums)
    nums = set(nums)
    output = []
    for i in range(1,n+1):
        if i not in nums:
            output.append(i)
    return output

nums = [4,3,2,7,8,2,3,1]
missingNumbers = findDisappearedNumbers(nums)
print(missingNumbers)
