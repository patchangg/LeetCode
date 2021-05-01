
def sumOfUnique(nums):
    dict = {}
    sum = 0
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    for key in dict:
        if dict[key] == 1:
            sum += key
    return sum

nums = [1,2,3,2]
uniqueSum = sumOfUnique(nums)
print(uniqueSum)
