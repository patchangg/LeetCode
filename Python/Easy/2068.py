from collections import Counter

def checkAlmostEquivalent(word1, word2):
    c = Counter(word1)
    c.subtract(word2)
    for key, value in c.most_common():
        if abs(value) > 3:
            return False
    return True

word1 = "aaaa"
word2 = "bccb"
isAlmostEquivalent = checkAlmostEquivalent(word1,word2)
print(isAlmostEquivalent)
