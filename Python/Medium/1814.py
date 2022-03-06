
def countNicePairs(nums):
    freq = {}
    output = 0
    for num in nums:
        pair = num - int(str(num)[::-1])
        if pair not in freq:
            freq[pair] = 1
        else:
            output += freq[pair]
            freq[pair] += 1
    return output % (10 ** 9 + 7)

# Store the nice pair of num - rev(num) in a frequency hashmap.
# If another number equals that pair add the current frequency to the output
# and add one to the frequency. This captures every pair it can make with
# other numbers in the array. O(n), O(n) space
nums = [42,11,1,97]
numNicePairs = countNicePairs(nums)
print(numNicePairs)
