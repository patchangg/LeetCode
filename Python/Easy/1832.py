
def checkIfPangram(sentence):
    return len(set(sentence)) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
isPanagram = checkIfPangram(sentence)
print(isPanagram)
