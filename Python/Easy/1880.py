
def isSumEqual(firstWord, secondWord, targetWord):
    values = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
    first = ""
    second = ""
    target = ""
    for i in firstWord:
        first += str(values[i])
    for j in secondWord:
        second += str(values[j])
    for k in targetWord:
        target += str(values[k])
    if int(first) + int(second) == int(target):
        return True
    else:
        return False

firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
equalSum = isSumEqual(firstWord,secondWord,targetWord)
print(equalSum)
