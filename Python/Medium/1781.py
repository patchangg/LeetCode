import collections

def beautySum(s):
    output = 0
    for i in range(len(s)-1):
        counted = collections.Counter()
        for j in range(i,len(s)):
            counted[s[j]] += 1
            output += max(counted.values()) - min(counted.values())
    return output

# Figure out every combination of the string and add the differences in beauty values
# Beauty values is the difference between the most frequent character and least
# O(n^2), O(1) space
s = "aabcbaa"
beauty = beautySum(s)
print(beauty)
