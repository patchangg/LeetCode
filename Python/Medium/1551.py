
def minOperations(n):
    arr = [(2*i)+1 for i in range(n)]
    target = sum(arr)/n
    if (n % 2) == 0:
        len = n/2
    else:
        len = n/2 + 0.5
    total = 0
    for s in range(int(len)):
        total += (n - arr[s])
    return total






n = 5
equal = minOperations(n)
print(equal)
