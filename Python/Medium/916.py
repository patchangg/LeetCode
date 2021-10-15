from collections import Counter

def wordSubsets(words1,words2):
    count = Counter()
    for word in words2:
        count |= Counter(word)
    return [word for word in words1 if not count - Counter(word)]

# Find the maximum amount of times each letter occurs in every word in the words2
# array, keeping the highest amount. E.g "gg", "g" results in g: 2 in the counter
# Then for every word in the word1 array, check if the counts is higher or equal
# to the frequency in the word2 for every letter, if so put it in the array
# Return all the words that have contain every string in words2 array
# O(n * m) where n is the length of words1 and m is the length of words2.
# O(n) space
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
universalStrings = wordSubsets(words1,words2)
print(universalStrings)
