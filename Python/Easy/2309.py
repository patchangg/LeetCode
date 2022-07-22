from collections import Counter

def greatestLetter(s):
    counted = Counter(s)
    for ch in reversed(ascii_uppercase):
        if counted[ch] and counted[ch.lower()]:
            return ch
    return ""

s = "lEeTcOdE"
greatest = greatestLetter(s)
print(greatest)
