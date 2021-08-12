
def longestCommonSubsequence(text1, text2):
    dp = [[0] * (len(text2)+1) for l in range(len(text1) + 1)]
    for i, c in enumerate(text1):
        for j, r in enumerate(text2):
            if c == r:
                dp[i+1][j+1] = dp[i][j] +1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    return dp[-1][-1]

# Longest Common Subsequence problem.
# For each letter in the first string, compare if it equals to the second string
# Keep going to check if the previous suequence is equal.
# Combine the longest Subsequence that both strings have once you reach the end
# Only can combine Subsequences that come after each other 
# O(n * m), O(n * m) space
text1 = "abcde"
text2 = "ace"
LCS = longestCommonSubsequence(text1,text2)
print(LCS)
