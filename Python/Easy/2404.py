
def mostFrequentEven(nums):
    counted = {}
    val = float('inf')
    freq = 0
    for num in nums:
        if num % 2 == 0:
            if num in counted:
                counted[num] += 1
            else:
                counted[num] = 1
            if counted[num] > freq or (counted[num] == freq and num < val):
                val = num
                freq = counted[num]
    if freq > 0:
        return val
    else:
        return -1

nums = [0,1,2,2,4,4,1]
mostFrequentEvenNum = mostFrequentEven(nums)
print(mostFrequentEvenNum)
