
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = [0,1]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
    return f[n]



n = 4
fibonacci = fib(n)
print(fibonacci)
