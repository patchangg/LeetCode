from collections import Counter

def numSplits(s):
    leftWindow = Counter()
    rightWindow = Counter(s)
    output = 0
    for i in s:
        leftWindow[i] += 1
        rightWindow[i] -= 1
        if rightWindow[i] == 0:
            del rightWindow[i]

        if len(leftWindow) == len(rightWindow):
            output += 1
    return output

s = "aacaba"
number = numSplits(s)
print(number)
