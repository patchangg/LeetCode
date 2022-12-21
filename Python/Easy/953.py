
def isAlienSorted(words, order):
    alien = {}
    for i,c in enumerate(order):
        alien[c] = i
    rearranged = []
    for word in words:
        n = []
        for c in word:
            n.append(alien[c])
        rearranged.append(n)
    for w1, w2 in zip(rearranged,rearranged[1:]):
        if w1 > w2:
            return False
    return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
isAlienLanguageSorted = isAlienSorted(words,order)
print(isAlienLanguageSorted)
