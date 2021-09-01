
def isValid(s):
    while s.find('abc') >= 0:
        s = s.replace('abc', '')
    return s == ''

# Find any instance of abc in the string and remove it from the string
# If the string is empty after removing all valid abc substrings
# that means it is valid . O(n^2), O(n^2)
s = "aabcbc"
valid = isValid(s)
print(valid)
