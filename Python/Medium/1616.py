
def checkPalindromeFormation(a, b):
    def canFormPalindrome(x, y):
        left = 0
        right = len(a) - 1
        while left < right and x[left] == y[right]:
            left += 1
            right -= 1
        s1 = x[left:right+1]
        s2 = y[left:right + 1]
        return s1 == s1[::-1] or s2 == s2[::-1]

    return canFormPalindrome(a, b) or canFormPalindrome(b, a)

# For each string, check the prefix and suffix match and see if the middle
# between the two index are palindromes, if so return True as prefix + suffix
# will make a possible palindrome. O(n), O(n) space
a = "x"
b = "y"
hasPalindrome = checkPalindromeFormation(a,b)
print(hasPalindrome)
