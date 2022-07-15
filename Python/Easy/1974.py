
def minTimeToType(word):
    output = len(word)
    prev = "a"
    for c in word:
        curr = (ord(c) - ord(prev)) % 26
        output += min(curr, 26 - curr)
        prev = c
    return output

word = "abc"
minTime = minTimeToType(word)
print(minTime)
