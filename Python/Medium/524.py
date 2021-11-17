
def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    dictionary.sort(key = lambda x: (-len(x), x))
    for word in dictionary:
        i = 0
        for c in s:
            if i < len(word) and word[i] == c:
                i += 1
        if i == len(word):
            return word
    return ""

# Sort the dictionary array by the word length descending.
# For each word, check if the letters to create the word in the string exist
# in order and if they do, return the word as that would be the current longest
# word that can be found in the string after deleting some letters
# O(nm) where n is the length of the dictionary and m is the length of the
# string, O(1) space
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
longestWord = findLongestWord(s,dictionary)
