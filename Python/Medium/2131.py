from collections import defaultdict

def longestPalindrome(words):
    dicts = defaultdict(int)
    center = 0
    output = 0
    for word in words:
        if word[0] == word[1]:
            if dicts[word] > 0:
                center -= 1
                dicts[word] -= 1
                output += 4
            else:
                dicts[word] += 1
                center += 1
        else:
            if dicts[word[::-1]] > 0:
                output += 4
                dicts[word[::-1]] -= 1
            else:
                dicts[word] += 1
    if center:
        output += 2
    return output

# Store each word in a hashmap. If the word consists of the same character,
# add it to the palindrome only if another one of it exists in the hashmap
# otherwise one of the words will be used in the center of the palindrome.
# If the reverse of the word is in the hashmap, put the pair in the palindrome
# O(n), O(n) space
words = ["lc","cl","gg"]
palindromeLength = longestPalindrome(words)
print(palindromeLength)
