from collections import Counter

def digitCount(num):
    counted = Counter(num)
    for i,d in enumerate(num):
        if counted[str(i)] != int(d):
            return False
    return True

num = "1210"
isNumCorrect = digitCount(num)
print(isNumCorrect)
