
def isHappy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1

n = 19
isHappyNumber = isHappy(n)
print(isHappyNumber)
