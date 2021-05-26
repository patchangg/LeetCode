import collections

def minSteps(s, t):
    c = collections.Counter(s)
    for char in t:
        if char in c:
            c[char] -= 1
    output = 0
    for key,value in c.items():
        if value > 0:
            output += value
    return output



s = "leetcode"
t = "practice"
minStep = minSteps(s,t)
print(minStep)
