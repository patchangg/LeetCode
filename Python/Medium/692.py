import collections

def topKFrequent(words, k):
    words = sorted(words)
    counted = Counter(words)
    output = []
    for word in counted.most_common(k):
        output.append(word[0])
    return output

# Sort the words so it is in lexicographical order,
# count the frequency of each words then return the k most frequent words.
# O(nlogn), O(1) space
words = ["i","love","leetcode","i","love","coding"]
k = 2
mostFrequentWords = topKFrequent(words,k)
print(mostFrequentWords)
