
def threeConsecutiveOdds(arr):
    if len(arr) < 2:
        return False
    for i in range(len(arr)-2):
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
            return True
    return False

arr = [2,6,4,1]
tripleOdds = threeConsecutiveOdds(arr)
print(tripleOdds)
