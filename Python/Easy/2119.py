
def isSameAfterReversals(num):
    reversed1 = int(str(num)[::-1])
    reversed2 = int(str(reversed1)[::-1])
    if reversed2 == num:
        return True
    else:
        return False

num = 526
sameAfterReversed = isSameAfterReversals(num)
print(sameAfterReversed)
