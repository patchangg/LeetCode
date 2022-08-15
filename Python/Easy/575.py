
def distributeCandies(candyType):
    diff = len(set(candyType))
    n = len(candyType) // 2
    if diff <= n:
        return diff
    else:
        return n

candyType = [1,1,2,2,3,3]
diffCandy = distributeCandies(candyType)
print(diffCandy)
