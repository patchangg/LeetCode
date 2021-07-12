import collections

def canConstruct(s, k):
    if len(s) < k:
        return False
    if k == len(s):
        return True
    counted = collections.Counter(s)
    odd = 0
    even = 0
    for letter in counted:
        if (counted[letter] % 2) == 0:
            even += 1
        else:
            odd += 1
    if (odd <= k <= len(s)):
        return True
    else:
        return False

# If k > len(s) it means that it is impossible to create any palidrome strings
# as the amount of possible combinations is impossible to meet k
# if k == len(s) then you can put s in any order to meet k strings
# K has to be less than or equal to the length or the string and
# greater than the odd count of the any character in the string as
# odd characters have to be wrapped between even count characters
# so min palidrome count will always be odd count
# and it has to be less than or equal to the string length as we can only get
# s length possible amount of palidrome strings. O(n + n) = O(n) time, O(n) space
s = "leetcode"
k = 3
constructed = canConstruct(s,k)
print(constructed)
