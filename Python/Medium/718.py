
def findLength(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    output = 0

    dp = [[0] * (n+1) for _ in range(m + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[j][i] = dp[j + 1][i + 1] + 1
            output = max(output,dp[j][i])
    return output

# Create a dp array length n*m.
# Go backwards from each array, whenever two numbers match, add 1 the dp location
# plus the dp diagonal from it to update the longest common subseqeunce.
# O(n*m), O(n*m) space
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
maximumLength = findLength(nums1,nums2)
print(maximumLength)
