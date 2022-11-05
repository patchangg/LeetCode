from collections import Counter

def rearrangeCharacters(s, target):
    counted = Counter(s)
    output = float(inf)
    for c, count in Counter(target).items():
        output = min(output,counted[c] // count)
    return output

s = "ilovecodingonleetcode"
target = "code"
numTargetStrings = rearrangeCharacters(s,target)
print(numTargetStrings)
