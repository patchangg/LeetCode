
def longestConsecutive(self, nums: List[int]) -> int:
    sets = set(nums)
    output = 0
    for num in nums:
        if num - 1 not in sets:
            curr = num
            while curr in sets:
                curr += 1
            output = max(output, curr - num)
    return output

# Change the array to a set so all lookups are O(1) time. This takes O(n) time.
# For each number in the set, check if there is no number before it so we don't
# repeat any sequences, then check for numbers one higher than it in the set.
# Store the longest consecutive sequence length and return the highest.
# O(n), O(n) space
nums = [100,4,200,1,3,2]
longestSequence = longestConsecutive(nums)
print(longestSequence)
