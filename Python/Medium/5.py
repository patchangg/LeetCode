
def longestPalindrome(s):
    output = ""
    def helper(s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    for i in range(len(s)):
        odd = helper(s,i,i)
        if len(temp) > len(output):
            output = odd
        even = helper(s,i,i+1)
        if len(temp) > len(output):
            output = even

    return output

# For each character in the string, check if a palindrome can be made from it
# and its neighbours. Check for odd and even length palindromes where odd has
# a single character in the middle while even has two. O(n^2), O(n) space
s = "babad"
string = longestPalindrome(s)
print(string)
