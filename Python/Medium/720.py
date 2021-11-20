
def longestWord(self, words: List[str]) -> str:
    words.sort()
    inSet = set([''])
    output = ""
    for word in words:
        if word[:-1] in inSet:
            if len(word) > len(output):
                output = word
            inSet.add(word)
    return output

# Sort the words from smallest to longest in lexicographical order.
# For each word in the array, if the letters before the last letter in the word,
# is in the set, add it to the set and check if the length is greater
# than the current longest word that has all its previous words in the array.
# If so, make that the new longest word in the array. O(nlogn), O(1) space
words = ["w","wo","wor","worl","world"]
longest = longestWord(words)
print(longest)
