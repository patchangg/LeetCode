
def halvesAreAlike(s):
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    n = len(s) // 2
    left = s[:n]
    right = s[n:]
    r = 0
    l = 0
    for c in left:
        if c in vowel:
            l += 1
    for c in right:
        if c in vowel:
            r += 1
    if r == l:
        return True
    else:
        return False

s = "book"
isAlike = halvesAreAlike(s)
print(isAlike)
