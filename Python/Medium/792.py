from collections import defaultdict

def numMatchingSubseq(s, words):
    array = defaultdict(list)
    output = 0

    for word in words:
        array[word[0]].append(word)

    for char in s:
        expected_words = array[char]
        array[char] = []
        for word in expected_words:
            if len(word) == 1:
                output += 1
            else:
                array[word[1]].append(word[1:])
    return output

# Create a dictionary and append the first character as the key and add the word
# For each character in the string, check if there is any words that start with it
# in the array. If the length of the word is 1, that means that word is a subsequence
# of the string, so increment the count by 1. Otherwise, append the rest of the
# word into the array with the key being the second letter of the word.
# This creates a loop where we get rid of the front letter until only 1 is left
# O(n + m * k^2 ) where n is the length of the string, m is the length of the
# words array and k^2 is the length of the longest word. O(n) space
s = "abcde"
words = ["a","bb","acd","ace"]
matchingSubsequence = numMatchingSubseq(s,words)
