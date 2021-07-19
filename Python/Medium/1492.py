
def kthFactor(n, k):
    output = []
    for i in range(1, n + 1):
        if n % i == 0:
            output.append(i)
    if len(output) >= k:
        return output[k-1]
    else:
        return -1

# Do a for loop until you reach n and if i divides n with no remainders
# it means that it is a factor of n.
# return the kth element of the factors array or -1 if it is out of bounds
# O(n), O(1) space
n = 4
k = 4
kth = kthFactor(n,k)
print(kth)
