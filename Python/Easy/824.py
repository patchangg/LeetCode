
def toGoatLatin(sentence):
    list = ["a","e","i","o","u","A","E","I","O","U"]
    counter = 1
    splitted = sentence.split(" ")
    output = []
    for word in splitted:
        if word[0] in list:
            line = word + "ma" + ("a" * counter)
            output.append(line)
        else:
            word += word[0]
            word = word[1:]
            line = word + "ma" + ("a" * counter)
            output.append(line)
        counter += 1
    return " ".join(output)


sentence = "The quick brown fox jumped over the lazy dog"
goated = toGoatLatin(sentence)
print(goated)
