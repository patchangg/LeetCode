
def largestMerge(self, word1: str, word2: str) -> str:
    output = ""
    while word1 and word2:
        if word1 > word2:
            output += word1[0]
            word1 = word1[1:]
        elif word1 < word2:
            output += word2[0]
            word2 = word2[1:]
        else:
            if len(word1) >= len(word2):
                output += word1[0]
                word1 = word1[1:]
            else:
                output += word2[0]
                word2 = word2[1:]
    output += word1
    output += word2
    return output

# Compare the two words, grab the first character from the largest word.
# If the first character is equal, grab from the largest string.
# At the end, append the rest of the word left onto the output.
# O((n + m) * min(n,m)) where min(n,m) is the string comparison and n + m is
# going through each string, O(n) space
word1 = "cabaa"
word2 = "bcaaa"
largestWord = largestMerge(word1,word2)
print(largestWord)
