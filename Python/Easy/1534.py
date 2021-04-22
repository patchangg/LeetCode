
def countGoodTriplets(arr, a, b, c):
    length = (len(arr) - 1)
    count = 0
    i = 0
    j = 1
    k = 2
    while i <= (length-2):
        while j <= (length-1):
            while k <= length:
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
                k += 1
            j += 1
            k = j + 1
        i += 1
        j = i + 1
        k = j + 1
    return count

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
count = countGoodTriplets(arr,a,b,c)
print(count)
