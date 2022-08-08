
def sortEvenOdd(nums):
    even = []
    odd = []
    output = []
    for i in range(len(nums)):
        if i % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    even = sorted(even)[::-1]
    odd = sorted(odd)
    for i in range(len(nums)):
        if i % 2 == 0:
            output.append(even.pop())
        else:
            output.append(odd.pop())
    return output

nums = [4,1,2,3]
evenOddSort = sortEvenOdd(nums)
print(evenOddSort)
