
def countCharacters(words, chars):
    dict = {}
    for char in chars:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    counted = 0
    for word in words:
        copyed = dict.copy()
        counter = True
        for char in word:
            if char in copyed:
                if copyed[char] > 0:
                    copyed[char] -= 1
                else:
                    counter = False
            else:
                counter = False
        if counter == True:
            counted += len(word)
    return counted



# words = ["cat","bt","hat","tree"]
# chars = "atach"
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
counted = countCharacters(words,chars)
print(counted)
