from collections import Counter

def percentageLetter(s, letter):
    counted = Counter(s)
    n = len(s)
    count = counted[letter]
    print(count,n)
    return int(count / n * 100)

s = "foobar"
letter = "o"
percentageOfLetter = percentageLetter(s,letter)
print(percentageOfLetter)
