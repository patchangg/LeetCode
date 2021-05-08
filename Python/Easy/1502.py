
def canMakeArithmeticProgression(arr):
    arr.sort()
    difference = arr[1] - arr[0]
    for i in range(2,len(arr)):
        if (arr[i] - arr[i-1]) != difference:
            return False
    return True



arr = [3,5,1]
can = canMakeArithmeticProgression(arr)
print(can)
