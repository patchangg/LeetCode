
def minimumLength(s):
    if len(s) == 1:
        return 1
    while len(s) > 1 and s[0] == s[-1]:
        s = s.strip(s[0])
    return len(s)

# Go through the string. If the prefix and suffix match, remove the character
# from the prefix and suffix. Repeat until the prefix and suffix characters
# don't match. O(n^2), O(n) space
s = "ca"
minLen = minimumLength(s)
print(minLen)
