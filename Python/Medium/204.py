
def countPrimes(n):
    if n < 3:
        return 0
    isPrime = [1] * n
    isPrime[0] = isPrime[1] = 0
    m = 2
    while m * m < n:
        for i in range(m * m, n,  m):
            isPrime[i] = 0
        if m == 2:
            m += 1
        else:
            m += 2
    return sum(isPrime)

# 0 amd 1 are not primes. Check if the number and its multiples are primes
# until m^2 is greater than n, returning the amount of primes strictly less than
# n. O(nlogn), O(n) space 
n = 10
numPrimes = countPrimes(n)
print(numPrimes)
