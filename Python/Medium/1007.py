from collections import Counter

def minDominoRotations(tops, bottoms):
    counted = Counter(tops) + Counter(bottoms)
    if counted.most_common(1)[0][1] < len(tops):
        return -1
    highest = counted.most_common(1)[0][0]
    topSwap = 0
    botSwap = 0
    for i,j in zip(tops,bottoms):
        if i == j == highest:
            continue
        elif i != highest and j != highest:
            return -1
        elif i != highest:
            topSwap += 1
        elif j != highest:
            botSwap += 1
    return min(topSwap,botSwap)

# Check if there are any integer that appear in both arrays that is equal or
# greater than their length.
# Use the most common integer that appears in both arrays as the integer to look
# for in each domino.
# Count the swaps for swapping the integer to the top or the bottom and return
# the smallest amount of swaps to get the row with the same integer
# O(nlogn), O(n) space
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
minRotations = minDominoRotations(tops,bottoms)
print(minRotations)
