from collections import permutations

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))

# Get every permutation of the nums array and create a set of it to get only
# unique elements. O(n!), O(n) space
nums = [1,1,2]
uniquePermutations = permuteUnique(nums)
print(uniquePermutations)
