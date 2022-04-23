
def longestWPI(self, hours: List[int]) -> int:
    output = 0
    score = 0
    seen = {}
    for i, h in enumerate(hours):
        if h > 8:
            score += 1
        else:
            score -= 1
        if score > 0:
            output = i + 1
        if score not in seen:
            seen[score] = i
        if score - 1 in seen:
            output = max(output, i - seen[score - 1])
    return output

# Increase the score when hours worked is over 8, decrease otherwise.
# This creates a postive and negative graph of multiple intervals of over
# 8 hours worked, recording the instance in a hashmap. If the previous
# score is seen, check if that is the longest wpi currently seen.
# O(n), O(n) space
hours = [9,9,6,0,6,6,9]
overEightDays = longestWPI(hours)
print(overEightDays)
