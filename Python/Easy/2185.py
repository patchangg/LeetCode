
def prefixCount(words, pref):
    output = 0
    n = len(pref)
    for word in words:
        if len(word) >= n:
            if word[:n] == pref:
                output += 1
    return output

words = ["pay","attention","practice","attend"]
pref = "at"
count = prefixCount(words,pref)
print(count)
