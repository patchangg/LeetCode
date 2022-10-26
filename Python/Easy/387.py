from collections import Counter

def firstUniqChar(s):
    counted = Counter(s)
    for i in range(len(s)):
        if counted[s[i]] == 1:
            return i
    return -1

s = "leetcode"
firstUniqueC = firstUniqChar(s)
print(firstUniqueC)
