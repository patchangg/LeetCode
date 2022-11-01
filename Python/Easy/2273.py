
def removeAnagrams(words):
    i = 0
    while i < len(words) - 1:
        if sorted(words[i]) == sorted(words[i + 1]):
            words.remove(words[i+1])
            continue
        i += 1
    return words

words = ["abba","baba","bbaa","cd","cd"]
noAnagramsArray = removeAnagrams(words)
print(noAnagramsArray)
