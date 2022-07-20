from collections import defaultdict

def countWords(words1, words2):
    hash1 = defaultdict(int)
    hash2 = defaultdict(int)
    output = 0
    for word in words1:
        hash1[word] += 1
    for word in words2:
        hash2[word] += 1
    if len(hash1) > len(hash2):
        for word in hash1:
            if hash1[word] == hash2[word] == 1:
                output += 1
    else:
        for word in hash2:
            if hash1[word] == hash2[word] == 1:
                output += 1
    return output

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
singleWord = countWords(words1,words2)
print(singleWord)
