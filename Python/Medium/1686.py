
def stoneGameVI(aliceValues, bobValues):
    pairs = sorted(zip(aliceValues,bobValues),key=sum,reverse=True)
    aliceSum = sum(i[0] for i in pairs[::2])
    bobSum = sum(i[1] for i in pairs[1::2])
    if aliceSum > bobSum:
        return 1
    elif bobSum > aliceSum:
        return -1
    else:
        return 0

# Greedy Problem
# Assume alice will take the value that is either highest value for her
# or highest value for bob, so sort the pairs into a+b
# O(nlogn), O(n) space
aliceValues = [1,3]
bobValues = [2,1]
winner = stoneGameVI(aliceValues,bobValues)
print(winner)
