
def countHomogenous(s):
    mod = 10**9 + 7
    output = 0
    char = ""
    count = 0
    for c in s:
        if c == char:
            count += 1
        else:
            char = c
            count = 1
        output = (output + count) % mod
    return output

# Go through the string and count homogenous substrings. If aa appears, that means
# we count aa and a. Since the output may be very large, return the output mod 10**9 + 7
# O(n), O(1) space
s = "abbcccaa"
numHomogenousSubstrings = countHomogenous(s)
print(numHomogenousSubstrings)
