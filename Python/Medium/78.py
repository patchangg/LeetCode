from itertools import chain, combinations

def subsets(nums):
    s = list(nums)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# Gets all possible subsets of the the lsit. O(n+1)
nums = [1,2,3]
subset = subsets(nums)
print(subset)
