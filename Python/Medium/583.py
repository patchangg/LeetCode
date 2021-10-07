
def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j] + (word1[i] == word2[j]))
    return m + n - 2 * dp[-1][-1]

# LCS problem, so create a n by m array to find the lcs of the two words
# If two letters are equal, increment the position else use the max of the
# index positions next the current index. The last index should contain
# the length of the longest common subsequence of the two words.
# Return m + n - 2 * lcs as we need to return how many letters we deleted to
# make both words equal. O(n*m), O(n+1*m+1) space
word1 = "sea"
word2 = "eat"
numDeletes = minDistance(word1,word2)
print(numDeletes)
