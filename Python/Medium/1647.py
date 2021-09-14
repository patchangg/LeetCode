from collections import Counter

def minDeletions(s):
    output = 0
    seen = []
    freq = Counter(s)
    for item in freq.most_common():
        num = item[1]
        while num in seen and num != 0:
            num -= 1
            output += 1
        if num not in seen and num != 0:
            seen.append(num)
    return output

# Count the frequencies of each letter in the string and loop each character
# from decending frequency order.
# If the frequency has not been seen yet, add it to a seen array else
# keep removing 1 from frequency until it is not in seen or has reached 0,
# adding 1 to the delete counter each loop. O(nlogn), O(n) space 
s = "aabbcc"
minDeletes = minDeletions(s)
print(minDeletes)
