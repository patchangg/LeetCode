
def sortArrayByParity(A):
    odd = []
    even = []
    for i in A:
        if (i % 2) == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd


A = [3,1,2,4]
parity = sortArrayByParity(A)
print(parity)
