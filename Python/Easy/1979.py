
def findGCD(nums):
    m = max(nums)
    n = min(nums)
    for i in range(n,1,-1):
        if n % i == 0 and m % i == 0:
            return i
    return 1

nums = [2,5,6,9,10]
gcd = findGCD(nums)
print(gcd)
