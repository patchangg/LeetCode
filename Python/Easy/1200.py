
def minimumAbsDifference(arr):
    arr.sort()
    minimumArr = []
    lowest = abs(arr[1] - arr[0])
    for i in range(len(arr)-1):
        if abs(arr[i+1] - arr[i]) < lowest:
            minimumArr = []
            minimumArr.append([arr[i],arr[i+1]])
            lowest = abs(arr[i+1] - arr[i])
        elif abs(arr[i+1] - arr[i]) == lowest:
            minimumArr.append([arr[i],arr[i+1]])
    return minimumArr

arr = [3,8,-10,23,19,-4,-14,27]
minimum = minimumAbsDifference(arr)
print(minimum)
