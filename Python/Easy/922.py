
def sortArrayByParityII(nums):
    even = []
    odd = []
    for num in nums:
        if (num % 2) == 0:
            even.append(num)
        else:
            odd.append(num)
    array = []
    for i in range(len(even)):
        array.append(even[i])
        array.append(odd[i])
    return array


nums = [4,2,5,7]
sorted = sortArrayByParityII(nums)
print(sorted)
