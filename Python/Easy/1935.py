
def canBeTypedWords(text, brokenLetters):
    text = text.split(" ")
    output = len(text)
    for word in text:
        for c in word:
            if c in brokenLetters:
                output -= 1
                break
    return output

text = "hello world"
brokenLetters = "ad"
numWords = canBeTypedWords(text,brokenLetters)
print(numWords)
