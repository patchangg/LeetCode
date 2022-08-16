from collections import defaultdict

def uncommonFromSentences(s1, s2):
    words = defaultdict(int)
    s1 = s1.split(" ")
    s2 = s2.split(" ")
    output = []
    for word in s1:
        words[word] += 1
    for word in s2:
        words[word] += 1
    for key,value in words.items():
        if value == 1:
            output.append(key)
    return output

s1 = "this apple is sweet"
s2 = "this apple is sour"
uncommonWords = uncommonFromSentences(s1,s2)
print(uncommonWords)
