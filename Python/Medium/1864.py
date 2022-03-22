from collections import Counter

def minSwaps(s):
    s = list(s)
    counted = Counter(s)
    output = [0] * 2

    if abs(counted['1']-counted['0']) > 1:
        return -1

    for i in range(0,len(s),2):
        if s[i] == '0':
            output[0] += 1
        else:
            output[1] += 1

    if counted['0'] == counted['1']:
        return min(output)
    if counted['0'] < counted['1']:
        return output[0]
    else:
        return output[1]

# Count the number of 1's and 0's in the string. If there is 2 or more number
# compared to the other, it is impossible.
# Loop through every second character in the string and check if it's 0
# or one. If there is more ones, we need to swap the number of 0's to get
# an alternating string, vice versa for 1. O(nlogn), O(n) space
s = "111000"
numSwaps = minSwaps(s)
print(numSwaps)
