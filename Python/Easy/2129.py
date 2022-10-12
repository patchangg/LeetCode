
def capitalizeTitle(title):
    sentence = title.split(" ")
    for i in range(len(sentence)):
        if len(sentence[i]) < 3:
            sentence[i] = sentence[i].lower()
        else:
            sentence[i] = sentence[i].title()
    return " ".join(sentence)

title = "capiTalIze tHe titLe"
capitalSentence = capitalSentence(title)
print(capitalSentence)
