
def arrangeWords(text):
    split = text.split()
    split[0] = split[0].lower()
    dicts = {}
    for word in split:
        if len(word) in dicts:
            dicts[len(word)].append(word)
        else:
            dicts[len(word)] = [word]
    arr = []
    for i in sorted(dicts.keys()):
        arr.append(" ".join(dicts[i]))
    output = " ".join(arr).capitalize()
    return output

# Split the input and store into a dictionary based on the length of the word
# Join the words back together based on the length of the word and
# capitalize the output string.
# O(2n) = O(n) where n is the amount of words in text, O(n) space
text = "Keep calm and code on"
arrangedWord = arrangeWords(text)
print(arrangedWord)
