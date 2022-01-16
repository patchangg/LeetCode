from collections import Counter

def isPossible(nums):
    numbers = Counter(nums)
    sequences = Counter()
    for num in nums:
        if numbers[num]:
            if sequences[num-1]:
                sequences[num-1] -=1
                sequences[num] += 1
            elif numbers[num+1] and numbers[num+2]:
                numbers[num+1] -= 1
                numbers[num+2] -= 1
                sequences[num+2] += 1
            else:
                return False
            numbers[num] -= 1
    return True

# Count the numbers in the array and create a dictionary that will store
# the end of the sequences.
# If the current number isn't a new end of a sequence or the 2 numbers higher
# than it does not exist in the counter dictionary, return False as it is
# impossible to create a split array. Otherwise update the dictionaries
# with a new sequence end. O(n), O(n) space
nums = [1,2,3,3,4,5]
canSplitNums = isPossible(nums)
print(canSplitNums)
