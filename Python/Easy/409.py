from collections import Counter

def longestPalindrome(s):
    counted = Counter(s)
    odds = 0
    for i, v in counted.items():
        if v % 2 == 1:
            odds += 1
    single = 0
    if odds:
        single += 1
    return len(s) - odds + single

s = "abccccdd"
palindromeLength = longestPalindrome(s)
print(palindromeLength)
