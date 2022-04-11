from collections import Counter

def balancedString(s):
    output = len(s)
    length = len(s)
    l = 0
    counted = Counter(s)
    for r, c in enumerate(s):
        counted[c] -= 1
        while l < length and all(length // 4 >= counted[c] for c in 'QWER'):
            output = min(output, r - l + 1)
            counted[s[l]] += 1
            l += 1
    return output

# Create a sliding window on the string, go along the string until there
# are equal or less number of characters remaining to make the balanced string
# to find the minimum substring length to change  the string into a balanced
# string. O(n), O(n) space
s = "QWER"
substringLength = balancedString(s)
print(substringLength)
