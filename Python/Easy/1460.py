
def canBeEqual(target, arr) :
    arr.sort()
    target.sort()
    if target == arr:
        return True
    else:
        return False

target = [392,360]
arr = [392,360]
isEqual = canBeEqual(target,arr)
print(isEqual)
