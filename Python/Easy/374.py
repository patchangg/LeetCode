# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pick = 6
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0

def guessNumber(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        g = guess(mid)
        if g == -1:
            high = mid - 1
        elif g == 1:
            low = mid + 1
        else:
            return mid
    return low

n = 10
pick = 6
guess = guessNumber(n)
print(guess)
