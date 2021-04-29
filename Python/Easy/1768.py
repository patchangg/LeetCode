
def mergeAlternately(word1, word2):
    word1arr = list(word1)
    word2arr = list(word2)
    merged = []
    while word1arr and word2arr:
        merged.append(word1arr[0])
        merged.append(word2arr[0])
        del word1arr[0]
        del word2arr[0]
    if word1arr:
        merged = merged + word1arr
    elif word2arr:
        merged = merged + word2arr
    return "".join(merged)

word1 = "ab"
word2 = "pqrs"
merged = mergeAlternately(word1,word2)
print(merged)
