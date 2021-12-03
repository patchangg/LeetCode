
def longestSubsequence(arr, difference)
    count = {}
    for num in arr:
        count[num] = 1 + count.get(num - difference, 0)
    return max(count.values())

# For each number in the array, put 1 plus the count of the number - the
# difference to calculate if there is a subsequence that has difference between
# each integer. O(n), O(n) space
arr = [1,2,3,4]
difference = 1
widestSubsequence = longestSubsequence(arr,difference)
