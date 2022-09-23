
def maxPower(s):
    output = 1
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
            output = max(output,count)
        else:
            count = 1
    return output

s = "leetcode"
longestConsectutiveCharacter = maxPower(s)
print(longestConsectutiveCharacter)
