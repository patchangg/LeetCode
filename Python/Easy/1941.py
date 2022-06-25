from collections import Counter

def areOccurrencesEqual(s):
    occurence = Counter(s)
    freq = occurence.most_common(1)[0][1]
    for c in occurence.most_common():
        if c[1] != freq:
            return False
    return True

s = "abacbc"
equalOccurences = areOccurrencesEqual(s)
print(equalOccurences)
