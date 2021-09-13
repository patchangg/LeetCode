
def maxProduct(words):
    output = 0
    for i in range(len(words)):
        setA = set(words[i])
        for j in range(i,len(words)):
            setB = set(words[j])
            if len(setA.intersection(setB)) == 0:
                output = max(output,len(words[i])*len(words[j]))
    return output

# For each string, compare it to the other strings in the array by
# transforming both strings into a set and checking if they share any
# characters, if they don't, multiply the length of each word by each other
# and compare to the current maximum. Return the highest value.
# O(nlogn), O(n) space
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
maximum = maxProduct(words)
print(maximum)
