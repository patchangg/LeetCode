
def numJewelsInStones(jewels, stones):
    jewel = set(jewels)
    stone = list(stones)
    count = 0
    for i in jewel:
        count += stone.count(i)
    print(count)


jewels = "aA"
stones = "aAAbbbb"
num = numJewelsInStones(jewels,stones)
