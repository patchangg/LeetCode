
def findLongestChain(self, pairs: List[List[int]]) -> int:
    if len(pairs) == 1:
        return 1
    output = 0
    pairs = sorted(pairs, key=lambda x:x[1])
    prev = -float('inf')
    for a,b in pairs:
        if a > prev:
            prev = b
            output += 1
    return output

# Sort the pairs by the second number as choosing the second number is better
# than choosing the first
# If pairA[1] < pair[0] then put pairA into the chain
# If pairA[1] >= pairB[0], append pairA to the chain as it would be smaller,
# having more opportunties to create a longer chain as pairA[1] < pairB[1]
# O(nlogn), O(n) space
pairs = [[1,2],[2,3],[3,4]]
longestChain = findLongestChain(pairs)
print(longestChain)
