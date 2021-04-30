
def repeatedNTimes(A):
    A.sort()
    i = 0
    while i < len(A):
        if A[i] == A[i+1]:
            return A[i]
        i += 1

A = [1,2,3,3]
repeated = repeatedNTimes(A)
print(repeated)
