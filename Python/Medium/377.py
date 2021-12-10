
def combinationSum4(self, nums: List[int], target: int) -> int:
    nums = sorted(nums)
    perms = [1] + [0] * target
    for i in range(target + 1):
        for num in nums:
            if num > i:
                break
            if num == i:
                perms[i] += 1
            if num < i:
                perms[i] += perms[i-num]
    return perms[target]

# Sort the nums array and create a zero array, length of the target + 1
# For each number to the target, check if getting that permutation with the
# numbers in the array is possible. If the number is larger than i, skip it.
# If the number is equal, add one to the array and if the number is smaller
# than i, that means you can add a permutation with i, i - num times.
# O(n * m) where n is target and m is the length of nums. O(n+1) space
nums = [1,2,3]
target = 4
possiblePerms = combinationSum4(nums,target)
print(possiblePerms)
