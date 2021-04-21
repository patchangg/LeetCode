
def sumOddLengthSubarrays(arr):
    length = len(arr)
    total = 0
    i = 1
    while i <= length:
        for s in range(length):
            if i > 1 and s + i <= length:
                total += sum(arr[s:i+s])
            elif i == 1:
                total += arr[s]
        i += 2
    return total

arr = [1,4,2,5,3]
sum = sumOddLengthSubarrays(arr)
