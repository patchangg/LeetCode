import string

def countPalindromicSubsequence(s):
    output = 0
    for c in string.ascii_lowercase:
        l = s.find(c)
        r = s.rfind(c)
        if l > -1:
            output += len(set(s[l+1:r]))
    return output

# For each letter in the alphabet, check if there is at least 2 occurences
# of it, one from the left side of the string and one from the right side of
# the string. If 2 are found, create a set of 3 letter palindromic
# subsequences of that letter. O(26n), O(26n) space
s = "aabca"
palindromicSubsequences = countPalindromicSubsequence(s)
print(palindromicSubsequences)
