from collections import Counter

def findAnagrams(s, p):
    output = []
    sCounter = Counter(s[:len(p)])
    pCounter = Counter(p)

    for i in range(len(p),len(s)):
        if sCounter == pCounter:
            output.append(i-len(p))
        sCounter[s[i-len(p)]] -= 1
        if sCounter[s[i-len(p)]] == 0:
            del sCounter[s[i-len(p)]]
        sCounter[s[i]] += 1

    if sCounter == pCounter:
        output.append(len(s)-len(p))

    return output

# Use a sliding window sized p and go through the string, checking if the
# window has the same characters as p. Update the Counters when moving the window
# Do a edge case check if the last window is a anagram. O(n), O(n) space
s = "cbaebabacd"
p = "abc"
anagrams = findAnagrams(s,p)
