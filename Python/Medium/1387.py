
def getKth(lo, hi, k):
    if lo == hi == k == 1:
        return 1
    powers = {}
    def findPower(x,count):
        if x == 1:
            return count
        count += 1
        if (x % 2) == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        if x in powers:
            return count + powers[x]
        return findPower(x,count)
    for x in range(lo,hi+1):
        powers[x] = findPower(x,0)
    return sorted(powers.items(),key=lambda x: x[1])[k-1][0]

# find the range between lo and hi by counting the amount of steps it takes to get to 1
# if x is even x // 2 else x = 3 * x + 1, store previous results in the dict
# for fast lookup. Once all the numbers have been calculated, sort the dict based on the key value
# then get the k-1th index of the dict and return its count number
# sorted is O(nlogn), for loop is O(hi-lo) or O(n), findPower is O(n)so n + n + nlogn = O(nlogn)
lo = 12
hi = 15
k = 2
kth = getKth(low,hi,k)
print(kth)
