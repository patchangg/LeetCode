
def numSub(s):
    output = 0
    for string in s.split('0'):
        output += ((len(string) + 1) * len(string)) // 2
    return output % (10**9 + 7)

# Split the string on 0 so we get strings of only 1's
# Use the formula n + 1 * n // 2 to get the number of substrings from the group
# of 1's. Mod the result by 10^9 + 7 to prevent integer overflow.
# O(n), O(n) space
s = "0110111"
numSubstrings = numSub(s)
print(numSubstrings)
