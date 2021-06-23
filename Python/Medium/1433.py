from collections import Counter

def check(x,y):
    sum = 0
    alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    for char in alphabet:
        sum += x[char] - y[char]
        if sum < 0:
            return False
    return True

def checkIfCanBreak(s1, s2):
    x = Counter(s1)
    y = Counter(s2)
    return check(x,y) | check(y,x)

# O(n)
# Count each character in the string and compare the alphabet index of each character
# if one string has stronger index than the other, it means that the sting can break the other
s1 = "abe"
s2 = "acd"
canBreak = checkIfCanBreak(s1,s2)
print(canBreak)
