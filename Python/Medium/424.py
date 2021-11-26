from collections import Counter

def characterReplacement(s, k):
    output = 0
    maxFreq = 0
    count = Counter()
    for i in range(len(s)):
        count[s[i]] += 1
        maxFreq = max(maxFreq,count[s[i]])
        if output < maxFreq + k:
            output += 1
        else:
            count[s[i-output]] -= 1
    return output

# Create a sliding window that keeps track of the length of the substring
# that includes k amount of changes. If the new character on the right side of
# the window exceeds the limit, remove the left side of the window.
# Keep count of the longest substring found and update it if a longer substring
# is found. O(n), O(n) space
s = "ABAB"
k = 2
longestSubstringLength = characterReplacement(s,k)
