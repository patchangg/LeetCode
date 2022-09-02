
def findOcurrences(text, first, second):
    output = []
    text = text.split(" ")
    for i in range(len(text)-2):
        if text[i] == first and text[i+1] == second:
            output.append(text[i+2])
    return output

text = "alice is a good girl she is a good student"
first = "a"
second = "good"
bigramOcurrences = findOcurrences(text,first,second)
print(bigramOcurrences)
