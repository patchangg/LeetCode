
def checkInclusion(s1, s2):
    str1 = [ord(s) - ord('a') for s in s1]
    str2 = [ord(s) - ord('a') for s in s2]

    counter = [0] * 26
    for string in str1:
        counter[string] += 1

    window = [0] * 26
    for i, s in enumerate(str2):
        window[s] += 1
        if i >= len(s1):
            window[str2[i - len(s1)]] -= 1
        if window == counter:
            return True
    return False

# Create a counter array for the two strings
# Count the frequency of each character in the first string
# Create a sliding window and check if the window is equal to the first string
# counter array. O(n + m) where n is length of s1 and m is length of s2
# O(m + m) space
s1 = "ab"
s2 = "eidbaooo"
permMatch = checkInclusion(s1,s2)
print(permMatch)
