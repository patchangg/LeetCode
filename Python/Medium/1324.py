
def printVertically(s):
    words = s.split()
    maxLen = max([len(word) for word in words])
    output = []
    for i in range(maxLen):
        order = []
        for word in words:
            if i < len(word):
                order.append(word[i])
            else:
                order.append(' ')
        output.append(''.join(order).rstrip())
    return output

# Get the maximum length of a word to know how many loops we have to do
# to get every index of the words. Combine the index character of each word
# together and append to to output with the right trailing spaces removed
# Trailing space needed to get the word in the same order as it was added in to the array
# O(n * m) where n is the amount of words and m is the max length of all the words
# O(1) space
s = "TO BE OR NOT TO BE"
verticalWords = printVertically(s)
print(verticalWords)
