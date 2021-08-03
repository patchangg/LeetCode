import collections

def reductionOperations(nums):
    counted = collections.Counter(nums)
    output = 0
    for index,num in enumerate(sorted(counted)):
        output += index * counted[num]
    return output

# Count the numbers in the nums array and sort it
# Using the index we can calculate how many times we need to reduce the number
# down to the next largest number.
# O(n + nlogn) = O(nlogn) as sorted average is n log n. O(n) space
nums = [1,1,2,2,3]
reductions = reductionOperations(nums)
print(reductions)
