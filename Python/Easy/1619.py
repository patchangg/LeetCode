
def trimMean(arr):
    arr = sorted(arr)
    remove = int(len(arr) * 0.05)
    return sum(arr[remove:-remove]) / (len(arr) - (remove * 2))

arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
mean = trimMean(arr)
print(mean)
