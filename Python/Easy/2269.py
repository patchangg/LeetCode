
def divisorSubstrings(num, k):
    n = str(num)
    output = 0
    for i in range(len(n)-k+1):
        mod = int(n[i:i+k])
        if mod != 0:
            if num % mod == 0:
                output += 1
    return output

num = 240
k = 2
kBeauties = divisorSubstrings(num,k)
print(kBeauties)
