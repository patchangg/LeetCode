
def peakIndexInMountainArray(arr):
    peak = 0
    for i in range(len(arr)):
        if arr[i] > arr[peak]:
            peak = i
    return peak

arr = [24,69,100,99,79,78,67,36,26,19]
peak = peakIndexInMountainArray(arr)
print(peak)
