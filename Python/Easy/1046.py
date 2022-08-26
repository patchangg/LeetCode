
def lastStoneWeight(stones):

    while len(stones) > 1:
        stones = sorted(stones)
        stones.append(abs(stones.pop() - stones.pop()))

    return stones[0]

stones = [2,7,4,1,8,1]
lastStone = lastStoneWeight(stones)
print(lastStone)
