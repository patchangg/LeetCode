
def isAnagram(s, t):
    if sorted(t) == sorted(s):
        return True
    return False

s = "anagram"
t = "nagaram"
validAnagram = isAnagram(s,t)
print(validAnagram)
