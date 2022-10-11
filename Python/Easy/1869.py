
def checkZeroOnes(s):
    ones = 0
    zeroes = 0
    bestOnes = 0
    bestZeroes = 0
    for c in s:
        if c == "1":
            ones += 1
            zeroes = 0
        else:
            zeroes += 1
            ones = 0
        bestOnes = max(ones,bestOnes)
        bestZeroes = max(zeroes,bestZeroes)
    return bestOnes > bestZeroes

s = "1101"
oneOverZero = checkZeroOnes(s)
print(oneOverZero)
