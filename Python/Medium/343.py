
def integerBreak(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    output = 1
    while n > 4:
        output *= 3
        n -= 3
    return output * n

# Factors of 2 and 3
# Multiplying the number by 3 until n is less than 5 will get the optimal solution
# Once it's less than 4, multiply it with the remaining n integer
# O(n), O(1) space
n = 10
maximumProduct = integerBreak(n)
print(maximumProduct)
