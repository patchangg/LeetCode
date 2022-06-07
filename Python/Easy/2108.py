
def firstPalindrome(words):
    for w in words:
        if w[::-1] == w:
            return w
    return ""

words = ["abc","car","ada","racecar","cool"]
palindrome = firstPalindrome(words)
print(palindrome)
