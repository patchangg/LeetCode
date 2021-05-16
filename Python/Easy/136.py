
def singleNumber(nums):
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    for key,value in dict.items():
        if value == 1:
            return key

nums = [2,2,1,3,3]
single = singleNumber(nums)
print(single)
