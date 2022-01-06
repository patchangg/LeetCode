from collections import deque

def bagOfTokensScore(tokens, power):
    output = 0
    queue = deque(sorted(tokens))
    score = 0
    while queue and (queue[0] <= power or score):
        if queue[0] <= power:
            power -= queue.popleft()
            score += 1
        else:
            power += queue.pop()
            score -= 1
        output = max(output,score)
    return output

# Sort the tokens array and transform it into a deque
# Greedily take the lowest tokens and if power is smaller than the first token
# in the queue and score is greater than 0, take the highest token.
# O(nlogn), O(n) space
tokens = [100]
power = 50
maximumScore = bagOfTokensScore(tokens,power)
print(maximumScore)
