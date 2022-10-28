
def minOperations(s):
    ones = 0
    zeroes = 0

    for i in range(len(s)):
        if int(s[i]) != i % 2:
            ones += 1
        else:
            zeroes += 1
    return min(ones,zeroes)

s = "0100"
numOperationsToAlternate = minOperations(s)
print(numOperationsToAlternate)
