
def maxScore(s):
    output = 0
    for i in range(1,len(s)):
        l = s[:i]
        r = s[i:]
        score = l.count('0') + r.count('1')
        output = max(output,score)
    return output

s = "011101"
maximumScore = maxScore(s)
print(maximumScore)
