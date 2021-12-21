
def longestBeautifulSubstring(word):
    vowels = ["a","e","i","o","u"]
    output = 0
    i = 0
    while i < len(word):
        if word[i] == "a":
            index = 0
            count = 1
            j = i + 1
            while j < len(word):
                if word[j] == vowels[index]:
                    count += 1
                elif index < 4:
                    if word[j] == vowels[index+1]:
                        index += 1
                        count += 1
                    else:
                        break
                else:
                    break
                j += 1
            if index == 4:
                output = max(output,count)
            i = j
        else:
            i += 1
    return output

# Loop through the word and when the character "a" is found, check its neighbours
# to see if there exists a beautiful substring. If a beautiful substring exists
# which is a substring containing at least 1 of every vowel, compare its length
# to the current maximum length and move the loop forward to the current inner
# loop position so we don't have to search those characters again. O(n), O(n) space
word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
lengthOfBeautifulSubstring = longestBeautifulSubstring(word)
print(lengthOfBeautifulSubstring)
