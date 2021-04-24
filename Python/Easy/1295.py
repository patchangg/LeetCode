
def findNumbers(nums):
    even = 0
    for num in nums:
        digit = len(str(num))
        if (digit % 2) == 0:
            even += 1
    return even

nums = [12,345,2,6,7896]
even = findNumbers(nums)
print(even)
