
def findKthPositive(arr, k):
    missing = []
    count = k
    for i in range(1,arr[-1]):
        if i not in arr:
            missing.append(i)
            count -= 1
    if count > 0:
        return arr[-1] + count
    else:
        return missing[k-1]

arr = [2,3,4,7,11]
k = 5
kthPositive = findKthPositive(arr,k)
print(kthPositive)
