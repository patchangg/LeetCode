
def maxVowels(s, k):
    vowels = "aeiou"
    output = 0
    for j in range(k):
        if s[j] in vowels:
            output += 1
    counter = output
    for i in range(len(s)-k):
        if s[i] in vowels:
            counter -= 1
        if s[i+k] in vowels:
            counter += 1
        output = max(counter,output)
    return output

# Count the amount of vowels in the first k letters as a base maximum vowels
# Create a sliding window and check if the current character and current + k
# is a vowel. If the current is a vowel, remove one from the counter as the window
# has one less vowel. If the current + k is a vowel, add one to the counter as the
# newest character is a vowel. Check if the counter is higher the previous max
# and replace it if it is. O(n), O(1) space
s = "abciiidef"
k = 3
maximum = maxVowels(s,k)
print(maximum)
