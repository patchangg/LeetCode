
def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
        return 0
    curr = 0
    output = 0
    index = {}
    for i, c in enumerate(s):
        if c in index and curr <= index[c]:
            curr = index[c] + 1
        else:
            output = max(output, i - curr + 1)
        index[c] = i
    return output

# Store the index of the latest seen character in a hashmap, using that
# to determine to move the window left or check the newest longest substring
# O(n), O(n) space
s = "abcabcbb"
longestSubstring = lengthOfLongestSubstring(s)
print(longestSubstring)
