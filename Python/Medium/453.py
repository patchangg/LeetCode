
def minMoves(nums):
    minimum = min(nums)
    output = 0
    for num in nums:
        output += num - minimum
    return output

# All numbers eventually have to reach the same number so just take the smallest
# number and add how many moves it has to take to get to that number for every
# number in the array. O(n), O(1) space
nums = [1,2,3]
numMoves = minMoves(nums)
print(numMoves)
