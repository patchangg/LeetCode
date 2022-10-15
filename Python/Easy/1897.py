
def makeEqual(words):
    hashm = {}
    n = len(words)
    for word in words:
        for c in word:
            if c not in hashm:
                hashm[c] = 1
            else:
                hashm[c] += 1

    for key, value in hashm.items():
        if value % n != 0:
            return False
    return True

words = ["abc","aabc","bc"]
equalCharacters = makeEqual(words)
print(equalCharacters)
