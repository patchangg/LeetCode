
def isPrefixOfWord(sentence, searchWord):
    n = len(searchWord)
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        if len(sentence[i]) >= n:
            if sentence[i][:n] == searchWord:
                return i + 1
    return -1

sentence = "i love eating burger"
searchWord = "burg"
prefixInSentence = isPrefixOfWord(sentence,searchWord)
print(prefixInSentence)
