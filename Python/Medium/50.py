
def myPow(x, n):
    m = abs(n)
    output = 1
    while m:
        if m % 2:
            output = output * x
        x = x * x
        m = m // 2
    if n >= 0:
        return output
    else:
        return 1 / output

# Power function. If n is negative, return it as a fraction. O(n), O(1) space
x = 2.00000
n = 10
power = myPow(x,n)
print(power)
