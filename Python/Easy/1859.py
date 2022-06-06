
def sortSentence(s):
    arr = s.split()
    output = [""] * len(arr)
    for w in arr:
        i = int(w[-1])-1
        output[i] = w[:-1]
    return " ".join(output)

s = "is2 sentence4 This1 a3"
sentence = sortSentence(s)
print(sentence)
