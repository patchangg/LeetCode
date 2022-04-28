
def minOperations(nums, x):
    total = sum(nums)
    output = -1
    curr = 0
    left = 0
    right = 0
    n = len(nums)
    if total == x:
        return n
    if x > total:
        return -1
    while right < n:
        curr += nums[right]
        while curr > total - x and left <= right:
            curr -= nums[left]
            left += 1
        if curr == (total - x):
            output = max(output, right - left + 1)
        right += 1
    if output == -1:
        return -1
    else:
        return n - output

# Use the total sum as the right edge. Two pointers to find the minimum subarray
# to get the total minus x which gets the subarray that can be removed to get
# x and the number of positions needed to form x. O(n), O(n) space
nums = [1,1,4,2,3]
x = 5
numOperations = minOperations(nums,x)
print(numOperations)
