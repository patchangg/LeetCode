
def equalSubstring(s, t, maxCost):
    l = 0
    cost = 0
    for r in range(len(s)):
        cost += abs(ord(s[r])-ord(t[r]))
        if cost > maxCost:
            cost -= abs(ord(s[l])-ord(t[l]))
            l += 1
    return r - l + 1

# Use a sliding window to find the maximum equal substring with maxCost to
# make the string equal. The window only grows if a higher length substring
# is found so in the end the gap between the sliding window will be the
# maximum substring length. O(n), O(1) space
s = "abcd"
t = "bcdf"
maxCost = 3
maxLenSubstring = equalSubstring(s,t,maxCost)
print(maxLenSubstring)
