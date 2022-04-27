from math import ceil

def repeatedStringMatch(a, b):
    repeat = ceil(len(b)/len(a))
    if b in (a * repeat):
        return repeat
    elif b in (a * (repeat + 1)):
        return repeat + 1
    return -1

# Use the length of a and b to find the minimum amount of times the a
# string should be repeated before it's in b, rounding up. If its not in
# there it must be in the amount of repeats + 1. O(1), O(1) space 
a = "abcd"
b = "cdabcdab"
numRepeats = repeatedStringMatch(a,b)
print(numRepeats)
