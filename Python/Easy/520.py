
def detectCapitalUse(word):
    if word[0].isupper() and word[1:].islower():
        return True
    if word.islower():
        return True
    for c in word:
        if c.islower():
            return False
    return True

word = "USA"
correctCapitalUsage = detectCapitalUse(word)
print(correctCapitalUsage)
