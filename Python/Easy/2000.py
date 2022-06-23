
def reversePrefix(word, ch):
    index = 0
    for i in range(len(word)):
        if word[i] == ch:
            index = i
            break
    if index == 0:
        return word
    left = word[:i+1][::-1]
    right = word[i+1:]
    return left + right

word = "abcdefd"
ch = "d"
reversed = reversePrefix(word,ch)
print(reversed)
