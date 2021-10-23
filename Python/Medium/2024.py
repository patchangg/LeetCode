from collections import Counter

def maxConsecutiveAnswers(answerKey, k):
    maxfreq = 0
    output = 0
    count = Counter()
    for i in range(len(answerKey)):
        count[answerKey[i]] += 1
        maxfreq = max(maxfreq,count[answerKey[i]])
        if output - maxfreq < k:
            output += 1
        else:
            count[answerKey[i-output]] -= 1
    return output

# Use a sliding window to determine the longest true/false chain in the answer
# key after changing k amount of answers. maxfreq keep track of the current
# longest chain and if there is a longer chain, update the output by 1
# else remove the first count of the sliding window. O(n), O(n) space
answerKey = "TTFF"
k = 2
consecutiveAnswers = maxConsecutiveAnswers(answerKey,k)
print(consecutiveAnswers)
