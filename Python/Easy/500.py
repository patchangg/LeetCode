
def findWords(words):
    first = set('qwertyuiop')
    second = set('asdfghjkl')
    third = set('zxcvbnm')
    output = []

    for word in words:
        w = set(word.lower())
        if w <= first or w <= second or w <= third:
            output.append(word)

    return output

words = ["Hello","Alaska","Dad","Peace"]
keyboardWords = findWords(words)
print(keyboardWords)
