
def findTheDifference(s, t):
    s = sorted(s)
    t = sorted(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[-1]

s = "abcd"
t = "abcde"
addedLetter = findTheDifference(s,t)
print(addedLetter)
