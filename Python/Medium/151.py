
def reverseWords(s):
    split = s.strip().split()
    return " ".join(split[::-1])

# Strip the word of any multiple spaces and split it based on a single space
# Reverse the array and then rejoin the array into a string. O(n), O(n) space
s = "the sky is blue"
reversed = reverseWords(s)
print(reversed)
