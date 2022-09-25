
def reverseOnlyLetters(s):
    s = list(s)
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l].isalpha() and s[r].isalpha():
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        elif not s[l].isalpha() and s[r].isalpha():
            l += 1
        elif not s[r].isalpha() and s[l].isalpha():
            r -= 1
        else:
            l += 1
            r -= 1
    return ''.join(s)

s = "ab-cd"
reversedLettersOnly = reverseOnlyLetters(s)
print(reversedLettersOnly)
