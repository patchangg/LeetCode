
def countPrefixes(words, s):
    output = 0
    for word in words:
        if s[:len(word)] == word:
            output += 1
    return output

words = ["a","b","c","ab","bc","abc"]
s = "abc"
numPrefixes = countPrefixes(words,s)
print(numPrefixes)
