
def maximumSubsequenceCount(text, pattern):
    c1 = 0
    c2 = 0
    output = 0
    for c in text:
        if c == pattern[0]:
            c2 += 1
        if c == pattern[1]:
            output += c2
            c1 += 1
            if pattern[1] == pattern[0]:
                output -= 1
    return output + max(c1,c2)

# Add the first character in the pattern at the front and the second character
# in the character at the back. Since the character is from the back, the first
# character can be used for every instance of it so we add the count to the
# output also. O(n), O(1) space
text = "abdcdbc"
pattern = "ac"
subsequenceCount = maximumSubsequenceCount(text,pattern)
print(subsequenceCount)
